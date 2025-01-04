from flask import Blueprint, request
from app.models import db, Post
from app.utils import success_response, error_response
from flask_login import login_required, current_user

post_routes = Blueprint("posts", __name__)

# Create a new post
# @post_routes.route("/", methods=["POST"])
# @login_required
# def create_post():
#     print(f"Current User: {current_user}")
#     if not current_user.is_authenticated:
#         return {"errors": {"message": "Unauthorized"}}, 401

#     data = request.get_json()
#     if not data or not data.get("content"):
#         return {"errors": {"message": "Content is required"}}, 400

#     post = Post(user_id=current_user.id, content=data["content"])

#     db.session.add(post)
#     db.session.commit()

#     return {"message": "Post created successfully", "post": post.to_dict()}, 201

@post_routes.route("/", methods=["POST"])
@login_required
def create_post():
    try:
        title = request.form.get('title')
        content = request.form.get('content')
        content_type = request.form.get('contentType')
        media = request.files.get('media')  # Handle media file

        if not title or not content or not content_type:
            return jsonify({"message": "All fields are required!"}), 400

        # Handle media upload (if any)
        if media:
            media.save(f'uploads/{media.filename}')  # Example of saving file

        post = Post(
            user_id=current_user.id,
            title=title,
            content=content,
            content_type=content_type,
            media=media.filename if media else None
        )
        db.session.add(post)
        db.session.commit()

        return post.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

@post_routes.route("/", methods=["GET"])
def get_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return success_response("Posts retrieved successfully! 🤗", [post.to_dict() for post in posts])
