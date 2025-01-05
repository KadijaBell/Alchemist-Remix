from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Reflection, ContentSource
from app.utils import get_content_source_or_404, success_response, error_response
from app.forms.reflection_form import ReflectionForm

reflection_routes = Blueprint("reflections", __name__)


#             GET ROUTES               #
#Get all reflections
@reflection_routes.route("/", methods=["GET"])
def get_reflections():
    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    each_page = request.args.get("each_page", 10, type=int)
    sort_by = request.args.get("sort_by", "created_at")
    order = request.args.get("order", "desc").lower()


    #validate sort_by
    valid_sort_by = ["created_at", "updated_at", "name"]
    if sort_by not in valid_sort_by:
        return error_response("Invalid sort field. Allowed fields: created_at, updated_at, name", 400)

  # Build query
    query = Reflection.query

    # Search reflections by content
    if search:
        query = query.filter(Reflection.content.ilike(f"%{search}%"))

    # Apply sorting
    sort_column = getattr(Reflection, sort_by)
    sort_column = sort_column.asc() if order == "asc" else sort_column.desc()

    # Paginate results
    reflections = query.order_by(sort_column).paginate(page=page, per_page=each_page, error_out=False)

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

# Get reflections by user
@reflection_routes.route("/user/<int:user_id>/", methods=["GET"])
def get_user_reflections(user_id):
    page = request.args.get("page", 1, type=int)
    each_page = request.args.get("each_page", 10, type=int)

    reflections = Reflection.query.filter_by(user_id=user_id).paginate(page=page, per_page=each_page, error_out=False)

    return success_response("Reflections retrieved successfully 🤗", {
        "reflections": [reflection.to_dict() for reflection in reflections.items],
        "total_pages": reflections.pages,
        "page": reflections.page,
        "each_page": each_page
    })


#             PUT ROUTES                #

# Update/Edit a reflection
@reflection_routes.route("/<int:id>/", methods=["PUT"])
@login_required
def update_reflection(id):
    reflection = Reflection.query.get(id)
    if not reflection:
        return error_response("Reflection not found", 404)

    # Ensure the reflection belongs to the logged-in user
    if reflection.user_id != current_user.id:
        return error_response("Unauthorized: You cannot update this reflection.", 403)

    form = ReflectionForm()
    form.csrf_token.data = request.cookies.get("csrf_token")
    form.user_id.data = current_user.id 

    if form.validate():  # Validate the form data
        reflection.content = form.content.data
        db.session.commit()
        return success_response("🪄 Reflection updated successfully.", reflection.to_dict())

    return error_response("Validation failed", 400, form.errors)


#             POST ROUTES               #
# Add a reflection

@reflection_routes.route("/<int:source_id>/", methods=["POST"])
@login_required
def add_reflection(source_id):
    source = get_content_source_or_404(source_id, ContentSource)
    if isinstance(source, dict):
        return source

    form = ReflectionForm()
    form.csrf_token.data = request.cookies.get("csrf_token")
    form.user_id.data = current_user.id
    if form.validate():
        new_reflection = Reflection(
            content=form.content.data,
            user_id=current_user.id,
            source_id=source_id
        )
        db.session.add(new_reflection)
        db.session.commit()
        return success_response("🪄 Reflection added successfully.", new_reflection.to_dict())
    return error_response("Validation failed", 400, form.errors)



#             DELETE ROUTES             #
# Delete a reflection
@reflection_routes.route("/<int:id>/", methods=["DELETE"])
def delete_reflection(id):
    reflection = Reflection.query.get(id)
    if not reflection:
        return error_response("Reflection not found", 404)

    db.session.delete(reflection)
    db.session.commit()
    return success_response("🗑️ Reflection deleted successfully.")
