from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User
from app.utils import get_content_source_or_404, success_response, error_response

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = get_content_source_or_404(id, User)
    if isinstance(user, dict): # error response
        return user
    return success_response("User retrieved successfully🤗",user.to_dict())
