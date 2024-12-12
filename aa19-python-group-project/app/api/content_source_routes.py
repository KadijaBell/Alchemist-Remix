from flask import Blueprint, jsonify, request
from app.models import db, ContentSource
from app.utils import get_content_source_or_404, success_response, error_response


content_source_routes = Blueprint("content_sources", __name__)


#             GET ROUTES               #

#Get all sources
@content_source_routes.route("/", methods=["GET"])
def get_sources():
    page = request.args.get("page", 1, type=int)
    each_page = request.args.get("each_page", 10, type=int)

    sources = ContentSource.query.paginate(page=page, per_page=each_page, error_out = False)

    return success_response("Sources retrieved successfully🤗",
    {
        "sources": [source.to_dict() for source in sources.items],
        "total_pages": sources.total,
        "page": sources.page,
        "each_page": each_page

    })
# @content_source_routes.route("/", methods=["GET"])
# def get_sources():
#     sources = ContentSource.query.all()
#     return success_response("Sources retrieved successfully🤗",{"sources": [source.to_dict() for source in sources]})


#Get a single source
@content_source_routes.route("/<int:id>", methods=["GET"])
def get_source(id):
    source = get_content_source_or_404(id, ContentSource)
    if isinstance(source, ContentSource):
        return source
    # if not source:
    #     return {"error": "🥲 That creative content can't be found. Please try again."}, 404

    source.glances += 1
    db.session.commit()
    return success_response("Source retrieved successfully🤗", source.to_dict())

#Searching/Filtering sources
@content_source_routes.route("/search", methods=["GET"])
def search_sources():
    search = request.args.get("search", "")
    source_filter = request.args.get("type", "")

    query = ContentSource.query

    if search:
        query = query.filter(ContentSource.name.ilike(f"%{search}%"))

    if source_filter:
        query = query.filter(ContentSource.source_type == source_filter)

    sources = query.all()

    return {"sources": [source.to_dict() for source in sources]}

#             POST ROUTES               #


#Create a new source
@content_source_routes.route("/", methods=["POST"])
def create_source():
    data = request.get_json()
    if not data or not all([data.get("name"), data.get("type"), data.get("url")]):
        return error_response( "🥲 Missing required fields.", 400)
    # if not data:
    #     return {"error": "🥲 Please provide valid data."}, 400

    # Use `get` to safely retrieve values
    new_source = ContentSource(
        name=data.get("name"),
        source_type=data.get("type"),  # Changed from "media_type" to match expected request key
        url=data.get("url")
    )

    if not new_source.name or not new_source.source_type or not new_source.url:
         return error_response( "🥲 Missing required fields.", 400)

    db.session.add(new_source)
    db.session.commit()
    return success_response("Source created successfully🤗",new_source.to_dict(), 201)

#Like a source
@content_source_routes.route("/<int:id>/like", methods=["POST"])
def like_source(id):
    source = ContentSource.query.get(id)
    if not source:
        return {"error": "🥲 That creative content can't be found. Please try again."}, 404

    source.elixirs += 1
    db.session.commit()
    return {"message": "Elixir added!🔮", "total_elixirs": source.elixirs}

#Share a source
@content_source_routes.route("/<int:id>/share", methods=["POST"])
def share_source(id):
    source = get_content_source_or_404(id, ContentSource)
    if isinstance(source, ContentSource):
        return source
    source.transmutations += 1  # Increment shares
    db.session.commit()
    return {"message": "🔄Content transmuted!🛸", "total_transmutations": source.transmutations}



#             PUT ROUTES               #

#Update the source
@content_source_routes.route("/<int:id>", methods=["PUT"])
def update_source(id):
    source = ContentSource.query.get(id)
    if not source:
        return {"error": "🥲 That creative content can't be found. Please try again."}, 404

    data = request.get_json()
    if not data:
        return {"error": "🥲 Please provide valid data."}, 400

    # Used for safer dictionary access
    source.name = data.get("name", source.name)
    source.source_type = data.get("type", source.source_type)
    source.url = data.get("url", source.url)

    db.session.commit()
    return source.to_dict()

#             DELETE ROUTES               #


#Delete the source
@content_source_routes.route("/<int:id>", methods=["DELETE"])
def delete_source(id):
    source = ContentSource.query.get(id)
    db.session.delete(source)
    db.session.commit()
    return jsonify({"message": "Creation Deleted Successfully 🤞🏾"})
