from flask import Blueprint, request
from app.models import db, ContentSource, User
from app.utils import (
    get_content_source_or_404,
    success_response,
    error_response
)

alchemy_routes = Blueprint("alchemy", __name__)

######## HELPER FUNCTIONS ########
def validate_sort_and_order(model, sort_by, order):
    """Validate sorting fields and return the column."""
    valid_sort_by = ["created_at", "updated_at"]
    if sort_by not in valid_sort_by:
        return None, error_response(f"Invalid sort field. Allowed fields: {', '.join(valid_sort_by)}", 400)

    sort_column = getattr(model, sort_by)
    return sort_column.asc() if order == "asc" else sort_column.desc(), None


def paginate_query(query, page, each_page):
    """Apply pagination to a query."""
    return query.paginate(page=page, per_page=each_page, error_out=False)


######## ROUTES ########
#           GET ROUTES           #
# GET all fusions
@alchemy_routes.route("/fusions", methods=["GET"])
def get_all_fusions():
    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    each_page = request.args.get("each_page", 10, type=int)
    sort_by = request.args.get("sort_by", "created_at")
    order = request.args.get("order", "desc")

    query = ContentSource.query.filter_by(source_type="Alchemy Fusion")

    if search:
        query = query.filter(ContentSource.name.ilike(f"%{search}%"))

    sort_column, error = validate_sort_and_order(ContentSource, sort_by, order)
    if error:
        return error
    query = query.order_by(sort_column)

    fusions = paginate_query(query, page, each_page)

    return success_response("Fusions retrieved successfully 🤗", {
        "fusions": [fusion.to_dict() for fusion in fusions.items] if fusions.items else [],
        "total_pages": fusions.pages,
        "page": fusions.page,
        "each_page": each_page
})
# GET all elixirs
@alchemy_routes.route("/elixirs", methods=["GET"])
def get_all_elixirs():
    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    each_page = request.args.get("each_page", 10, type=int)
    sort_by = request.args.get("sort_by", "created_at")
    order = request.args.get("order", "desc")

    query = ContentSource.query.filter_by(source_type="Weighted Elixir")

    if search:
        query = query.filter(ContentSource.name.ilike(f"%{search}%"))

    sort_column, error = validate_sort_and_order(ContentSource, sort_by, order)
    if error:
        return error
    query = query.order_by(sort_column)

    elixirs = paginate_query(query, page, each_page)

    return success_response("Elixirs retrieved successfully 🤗", {
        "elixirs": [elixir.to_dict() for elixir in elixirs.items],
        "total_pages": elixirs.pages,
        "page": elixirs.page,
        "each_page": each_page
    })

# GET a specific fusion
@alchemy_routes.route("/fusions/<int:id>", methods=["GET"])
def get_fusion_by_id(id):
    fusion = get_content_source_or_404(id, ContentSource)
    if isinstance(fusion, dict) or fusion.source_type != "Alchemy Fusion":
        return error_response("Fusion not found.", 404)
    return success_response("Fusion retrieved successfully 🤗", fusion.to_dict())

# GET a specific elixir
@alchemy_routes.route("/elixirs/<int:id>", methods=["GET"])
def get_weighted_elixir_by_id(id):
    elixir = get_content_source_or_404(id, ContentSource)
    if isinstance(elixir, dict) or elixir.source_type != "Weighted Elixir":
        return error_response("Elixir not found.", 404)
    return success_response("Elixir retrieved successfully 🤗", elixir.to_dict())

# POST - Combine content sources into fusion
@alchemy_routes.route("/fusions", methods=["POST"])
def alchemy_fusion():
    data = request.get_json()
    source_ids = data.get("source_ids", [])

    if not source_ids or len(source_ids) < 2:
        return error_response("👎🏾 At least two sources are required for a fusion.", 400)

    sources = ContentSource.query.filter(ContentSource.id.in_(source_ids)).all()
    if len(sources) < len(source_ids):
        return error_response("🥲 One or more sources could not be found.", 404)

    fusion_source = ContentSource(
        name=" + ".join([source.name for source in sources]),
        source_type="Alchemy Fusion",
        url=", ".join([source.url for source in sources])
    )

    db.session.add(fusion_source)
    db.session.commit()
    return success_response("Fusion created successfully.", fusion_source.to_dict(), 201)

#           POST ROUTES            #

# POST - Add weighted elixirs
@alchemy_routes.route("/<int:id>/elixirs", methods=["POST"])
def add_weighted_like(id):
    source = get_content_source_or_404(id, ContentSource)
    if isinstance(source, dict):
        return source

    data = request.get_json()
    user = User.query.get(data.get("user_id"))
    if not user:
        return error_response("User not found.", 404)

    source.weighted_elixirs += 3.0 if user.role == "admin" else 1.0
    db.session.commit()
    return success_response("Elixir added successfully.", {"total_weighted_elixirs": source.weighted_elixirs})
#          PUT ROUTES             #

# PUT - Update fusion
@alchemy_routes.route("/fusions/<int:id>", methods=["PUT"])
def update_fusion(id):
    fusion = get_content_source_or_404(id, ContentSource)
    if isinstance(fusion, dict):
        return fusion

    data = request.get_json()
    fusion.name = data.get("name", fusion.name)
    fusion.url = data.get("url", fusion.url)
    db.session.commit()
    return success_response("Fusion updated successfully.", fusion.to_dict())

#           DELETE ROUTES            #

# DELETE - Delete fusion
@alchemy_routes.route("/fusions/<int:id>", methods=["DELETE"])
def delete_fusion(id):
    fusion = get_content_source_or_404(id, ContentSource)
    if isinstance(fusion, dict):
        return fusion

    db.session.delete(fusion)
    db.session.commit()
    return success_response("Fusion deleted successfully.")
