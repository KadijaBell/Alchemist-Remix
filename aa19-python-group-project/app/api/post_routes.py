from flask import Blueprint, request, jsonify
from app.models import db, Post
from app.utils import success_response, error_response
from flask_login import login_required, current_user

post_routes = Blueprint("posts", __name__)

# Helper function to fetch post
def fetch_post(id):
    post = Post.query.get(id)
    if not post:
        return error_response("🥲 That post can't be found. Please try again.", 404)
    return post

@post_routes.route('/', methods=['POST'])
@login_required
def create_post():
    data = request.form or request.json
    title = data.get('title')
    content = data.get('content')
    content_type = data.get('contentType')
    media = request.files.get('media')

    if not title or not content or not content_type:
        return error_response("All fields are required.", 400)

    post = Post(
        title=title,
        content=content,
        content_type=content_type,
        user_id=current_user.id,
        media=media.filename if media else None
    )
    db.session.add(post)
    db.session.commit()

    return success_response("Post created successfully🤗", post.to_dict(), 201)

@post_routes.route("/", methods=["GET"])
def get_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return success_response("Posts retrieved successfully! 🤗", [post.to_dict() for post in posts])
