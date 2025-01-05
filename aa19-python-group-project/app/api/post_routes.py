from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Post
from app.forms.post_form import PostForm
from app.utils import success_response, error_response

post_routes = Blueprint("posts", __name__)

#           GET ROUTES             #
@post_routes.route('/', methods=['GET'])
@login_required
def get_posts():
    user_id = current_user.id
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    content_type = request.args.get('content_type')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = Post.query.filter_by(user_id=user_id)
    if content_type:
        query = query.filter(Post.content_type == content_type)
    if start_date and end_date:
        query = query.filter(Post.created_at.between(start_date, end_date))

    posts = query.paginate(page=page, per_page=per_page, error_out=False)
    return {'posts': [post.to_dict() for post in posts.items], 'total': posts.total}


#           POST ROUTES          #
@post_routes.route("/", methods=["POST"])
@login_required
def create_post():
    form = PostForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        new_post = Post(
            user_id=current_user.id,
            title=form.data['title'],
            content=form.data['content'],
            content_type=form.data['content_type'],
            media=form.data.get('media'),
        )
        db.session.add(new_post)
        db.session.commit()
        return success_response({"post": new_post.to_dict()}, 201)

    return error_response(form.errors, 400)

#       PUT ROUTES          #
@post_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_post(id):
    post = Post.query.get(id)
    if not post or post.user_id != current_user.id:
        return error_response("Post not found or unauthorized", 404)

    form = PostForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        post.title = form.data.get('title', post.title)
        post.content = form.data.get('content', post.content)
        post.content_type = form.data.get('content_type', post.content_type)
        post.media = form.data.get('media', post.media)
        db.session.commit()
        return success_response({"post": post.to_dict()})

    return error_response(form.errors, 400)

#         DELETE ROUTES             #
@post_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_post(id):
    post = Post.query.get(id)
    if not post or post.user_id != current_user.id:
        return error_response("Post not found or unauthorized", 404)

    #Soft Delete
    post.is_active = False
    db.session.commit()

#Hard session delete
    db.session.delete(post)
    db.session.commit()
    return success_response({"message": "Post deleted successfully"})
