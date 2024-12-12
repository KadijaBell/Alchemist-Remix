from flask import Blueprint,request
from app.models import db, ContentSource, User
from app.utils import get_content_source_or_404, success_response, error_response, validate_data

alchemy_routes = Blueprint("alchemy", __name__)


######## UNIQUE FEATURE ROUTES ########

#             GET ROUTES               #





#             POST ROUTES               #

#Combine Content Sources

# Combine Content Sources
@alchemy_routes.route("/fusions", methods=["POST"])
def alchemy_fusion():
    data = request.get_json()
    source_ids = data.get("source_ids", [])

    if not source_ids or len(source_ids) < 2:
        return error_response("👎🏾 At least two sources are required for a fusion.", 400)

    sources = ContentSource.query.filter(ContentSource.id.in_(source_ids)).all()
    if len(sources) < len(source_ids):
        return error_response("🥲 One or more sources could not be found.", 404)

    fusion_name = " + ".join([source.name for source in sources])
    fusion_url = ", ".join([source.url for source in sources])

    fusion_source = ContentSource(
        name=fusion_name,
        source_type="Alchemy Fusion",
        url=fusion_url
    )
    db.session.add(fusion_source)
    db.session.commit()

    return success_response("Fusion created successfully.", fusion_source.to_dict())

# Weighted Elixirs of a source
@alchemy_routes.route("/<int:id>/elixirs", methods=["POST"])
def add_weighted_like(id):
    source = get_content_source_or_404(id, ContentSource)
    if isinstance(source, dict):  # If it's an error response
        return source

    data = request.get_json()
    user_id = data.get("user_id")
    user = User.query.get(user_id)
    if not user:
        return error_response("User not found.", 404)

    weight = 3.0 if user.role == "admin" else 1.0
    source.weighted_elixirs += weight

    db.session.commit()
    return success_response(f"Elixir added with weight {weight}!", {"total_weighted_elixirs": source.weighted_elixirs})

#             PUT ROUTES                #
# Update Fusion
@alchemy_routes.route("/fusions/<int:id>", methods=["PUT"])
def update_fusion(id):
    fusion = get_content_source_or_404(id, ContentSource)
    if isinstance(fusion, dict):  # Handles error response
        return fusion

    data = request.get_json()
    fusion.name = data.get("name", fusion.name)
    fusion.url = data.get("url", fusion.url)

    db.session.commit()
    return success_response("Fusion updated successfully.", fusion.to_dict())

#             DELETE ROUTES             #
# Delete Fusion
@alchemy_routes.route("/fusions/<int:id>", methods=["DELETE"])
def delete_fusion(id):
    fusion = get_content_source_or_404(id, ContentSource)
    if isinstance(fusion, dict):  # Handles error response
        return fusion

    db.session.delete(fusion)
    db.session.commit()
    return success_response("Fusion deleted successfully.")
