from flask import Blueprint, request, jsonify, session
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
import re
auth_routes = Blueprint('auth', __name__)

def validate_password(password):
    """
    Validates the password based on certain criteria.
    """
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    return None



@auth_routes.route('/', methods=['GET'])
def authenticate():
    """
    Authenticates a user.
    """
    # if current_user.is_authenticated:
    #     return current_user.to_dict()
    # else:
    #     return jsonify({"user": None}), 200

    # if current_user.is_authenticated:
    #     return current_user.to_dict()
    # return {'errors': {'message': 'Unauthorized'}}, 401
    # print(f"User authenticated? {current_user.is_authenticated}")
    # if current_user.is_authenticated:
    #     print(f"Authenticated user: {current_user}")
    #     return current_user.to_dict()
    # print("Unauthorized request")
    # return {'error': 'Unauthorized'}, 401
    # print(f"User authenticated? {current_user.is_authenticated}")

    print(f"Session Data: {session}")  # Debugging step
    if current_user.is_authenticated:
        print(f"Authenticated user: {current_user}")
        return current_user.to_dict()
    else:
        print("No user is logged in.")
        return {"error": "User not authenticated"}, 401




@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return form.errors, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


# @auth_routes.route('/signup', methods=['POST'])
# def sign_up():
#     """
#     Creates a new user and logs them in
#     """
#     form = SignUpForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     if form.validate_on_submit():
#         user = User(
#             username=form.data['username'],
#             email=form.data['email'],
#             password=form.data['password']
#         )
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)
#         return user.to_dict()
#     return form.errors, 401
@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    # Check form validation
    if not form.validate_on_submit():
        return jsonify({"errors": form.errors}), 400

    # Password validation logic
    password_error = validate_password(form.data['password'])
    if password_error:
        return jsonify({"errors": {"password": password_error}}), 400

    if form.validate_on_submit():
        # Check if the email already exists
        existing_email = User.query.filter_by(email=form.data['email']).first()
        if existing_email:
            return {"errors": {"email": "✨ This email is already in use. Choose another or recover your account."}}, 400

        # Check if the username already exists
        existing_username = User.query.filter_by(username=form.data['username']).first()
        if existing_username:
            return {"errors": {"username": "✨ This username is already taken. Choose a unique one."}}, 400

    # Create user
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return jsonify(user.to_dict()), 201

    return jsonify({"errors": form.errors}), 400




@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': {'message': 'Unauthorized'}}, 401
