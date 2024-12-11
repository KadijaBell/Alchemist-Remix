from flask import Blueprint,request
from app.models import db, ContentSource, Comment
from app.utils import success_response, error_response, get_content_source_or_404



comment_routes = Blueprint("comments", __name__)

#             GET ROUTES               #

#Get Comments of a source
@comment_routes.route("/<int:id>/comments", methods=["GET"])
def get_source_comments(id):
    source = get_content_source_or_404(id, ContentSource)
    if isinstance(source, dict): # error response
        return source

    return success_response("Comments retrieved successfully🤗",{"comments": [comment.to_dict() for comment in source.comments]}

    )

#             POST ROUTES               #

#Comments of a post
@comment_routes.route("/<int:id>/", methods=["POST"])
def comment_source(id):
    source = get_content_source_or_404(id, ContentSource)
    if isinstance(source, dict): # error response
        return source

    data = request.get_json()
    if not data or "content" not in data or "user_id" not in data:
        return error_response("🥲 Please provide valid content and user_id.", 400)

    new_comment = Comment(
        content=data["content"],
        user_id=data["user_id"],
        source_id=id
    )

    db.session.add(new_comment)
    db.session.commit()
    return success_response("Comment added successfully🤗",new_comment.to_dict(), 201)

#             PUT ROUTES                #
@comment_routes.route("/<int:id>/", methods=["PUT"])
def update_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return {"error": "Comment not found"}, 404

    data = request.get_json()
    comment.content = data.get("content", comment.content)
    db.session.commit()
    return comment.to_dict()


#             DELETE ROUTES             #

@comment_routes.route("/<int:id>/", methods=["DELETE"])
def delete_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return {"error": "Comment not found"}, 404

    db.session.delete(comment)
    db.session.commit()
    return {"message": "🚮Comment deleted successfully🚮"}
