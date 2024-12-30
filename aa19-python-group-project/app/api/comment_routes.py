from flask import Blueprint, request
from app.models import db, ContentSource, Comment
from app.utils import success_response, error_response, get_content_source_or_404

comment_routes = Blueprint("comments", __name__)

# --------- HELPER FUNCTIONS ---------- #
def validate_sorting(sort_by, valid_fields, order):
    """Validate and return the sorting column."""
    if sort_by not in valid_fields:
        return None, error_response(f"Invalid sort field. Allowed fields: {', '.join(valid_fields)}", 400)
    sort_column = getattr(Comment, sort_by)
    return sort_column.asc() if order == "asc" else sort_column.desc(), None

def validate_comment_data(data):
    """Ensure comment data has required fields."""
    if not data or "content" not in data or "user_id" not in data:
        return error_response("🥲 Please provide valid content and user_id.", 400)
    return None


# --------- GET ROUTES ---------- #

# Get all comments
@comment_routes.route("/", methods=["GET"])
def get_comments():
    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    each_page = request.args.get("each_page", 10, type=int)
    sort_by = request.args.get("sort_by", "created_at")
    order = request.args.get("order", "desc")

    query = Comment.query

    # Search comments
    if search:
        query = query.filter(Comment.content.ilike(f"%{search}%"))

    # Sorting
    valid_sort_by = ["created_at", "updated_at"]
    sort_column, error = validate_sorting(sort_by, valid_sort_by, order)
    if error:
        return error
    query = query.order_by(sort_column)

    # Pagination
    comments = query.paginate(page=page, per_page=each_page, error_out=False)

    return success_response("Comments retrieved successfully 🤗", {
        "comments": [comment.to_dict() for comment in comments.items],
        "total_pages": comments.pages,
        "page": comments.page,
        "each_page": each_page
    })


# Get comments for a specific source
@comment_routes.route("/<int:source_id>/comments", methods=["GET"])
def get_source_comments(source_id):
    source = get_content_source_or_404(source_id, ContentSource)
    if isinstance(source, dict):  # Error response
        return source

    comments = [comment.to_dict() for comment in source.comments]
    return success_response("Comments retrieved successfully 🤗", {"comments": comments})


# --------- POST ROUTES ---------- #

# Add a comment to a specific source
@comment_routes.route("/<int:source_id>/comments", methods=["POST"])
def comment_source(source_id):
    source = get_content_source_or_404(source_id, ContentSource)
    if isinstance(source, dict):  # Error response
        return source

    data = request.get_json()
    error = validate_comment_data(data)
    if error:
        return error

    new_comment = Comment(
        content=data["content"],
        user_id=data["user_id"],
        source_id=source_id
    )
    db.session.add(new_comment)
    db.session.commit()
    return success_response("Comment added successfully 🤗", new_comment.to_dict(), 201)


# --------- PUT ROUTES ---------- #

# Update a comment
@comment_routes.route("/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return error_response("Comment not found", 404)

    data = request.get_json()
    comment.content = data.get("content", comment.content)

    db.session.commit()
    return success_response("Comment updated successfully 🤗", comment.to_dict())


# --------- DELETE ROUTES ---------- #

# Delete a comment
@comment_routes.route("/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return error_response("Comment not found", 404)

    db.session.delete(comment)
    db.session.commit()
    return success_response("🚮 Comment deleted successfully 🚮")
