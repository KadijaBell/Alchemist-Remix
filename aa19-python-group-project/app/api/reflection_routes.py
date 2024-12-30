from flask import Blueprint, jsonify, request
from app.models import db, Reflection, ContentSource
from app.utils import get_content_source_or_404, success_response, error_response

reflection_routes = Blueprint("reflections", __name__)


#             GET ROUTES               #
#Get all reflections
@reflection_routes.route("/", methods=["GET"])
def get_reflections():
    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    each_page = request.args.get("each_page", 10, type=int)
    sort_by = request.args.get("sort_by", "created_at")
    order = request.args.get("order", "desc")
    query = Reflection.query

    # Search/Sort reflections by content
    if search:
        query = query.filter(Reflection.content.ilike(f"%{search}%"))
    if sort_by:
        query = query.order_by(getattr(Reflection, sort_by))

    #validate sort_by
    valid_sort_by = ["created_at", "updated_at", "name"]
    if sort_by not in valid_sort_by:
        return error_response("Invalid sort field. Allowed fields: created_at, updated_at, name", 400)


    # Build sorting dynamically
    sort_column = getattr(Reflection, sort_by, None)
    if sort_column is None:
        return error_response("Invalid sort column", 400)

    if order == "asc":
        sort_column = sort_column.asc()
    else:
        sort_column = sort_column.desc()

    # Pagination
    reflections = query.paginate(page=page, per_page=each_page, error_out=False)
    # Query with sorting
    reflections = Reflection.query.order_by(sort_column).paginate(page=page, per_page=each_page, error_out=False)

    return success_response("Reflections retrieved successfully 🤗", {
        "reflections": [reflection.to_dict() for reflection in reflections.items],
        "total_pages": reflections.pages,
        "page": reflections.page,
        "each_page": each_page
    })


#Get Reflections of a source
@reflection_routes.route("/<int:id>/", methods=["GET"])
def get_source_reflections(id):
    source = get_content_source_or_404(id, ContentSource)
    if isinstance(source, dict):  # Handles error response
        return source

    return success_response("Reflections retrieved successfully.", {
        "reflections": [reflection.to_dict() for reflection in source.reflections]
    })




#             PUT ROUTES                #

# Update/Edit a reflection
@reflection_routes.route("/<int:id>/", methods=["PUT"])
def update_reflection(id):
    reflection = Reflection.query.get(id)
    if not reflection:
        return {"error": "Reflection not found"}, 404

    data = request.get_json()
    reflection.content = data.get("content")
    db.session.commit()
    return reflection.to_dict()




#             POST ROUTES               #
# Add a reflection
@reflection_routes.route("/<int:source_id>/", methods=["POST"])
def add_reflection(source_id):
    source = get_content_source_or_404(source_id, ContentSource)
    if isinstance(source, dict):  # Handles error response
        return source

    data = request.get_json()
    new_reflection = Reflection(
        content=data.get("content"),
        user_id=data.get("user_id"),
        source_id=source_id
    )
    db.session.add(new_reflection)
    db.session.commit()
    return success_response("Reflection added successfully.", new_reflection.to_dict())




#             DELETE ROUTES             #
# Delete a reflection
@reflection_routes.route("/<int:id>/", methods=["DELETE"])
def delete_reflection(id):
    reflection = Reflection.query.get(id)
    if not reflection:
        return {"error": "Reflection not found"}, 404

    db.session.delete(reflection)
    db.session.commit()
    return {"message": "Reflection deleted successfully"}
