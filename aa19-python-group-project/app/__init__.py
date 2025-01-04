import os
from flask import Flask,  request, session, redirect, send_from_directory
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from .models import db, User
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.content_source_routes import content_source_routes
from .api.reflection_routes import reflection_routes
from .api.comment_routes import comment_routes
from .api.alchemy_routes import alchemy_routes
from .api.post_routes import post_routes
from .utils import error_response
from .seeds import seed_commands
from .config import Config
from werkzeug.exceptions import HTTPException



app = Flask(__name__, static_folder='../react-vite/dist', static_url_path='/')
app = Flask(__name__, static_folder='static')


# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'

@login.user_loader
def load_user(id):
    print(f"Loading user with ID: {id}")
    return User.query.get(int(id))

# Tell flask about our seed commands
app.cli.add_command(seed_commands)

# Set the path for uploaded media files
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')



app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  #16MB Maximum

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(content_source_routes, url_prefix='/api/content_sources')
app.register_blueprint(reflection_routes, url_prefix='/api/reflections')
app.register_blueprint(comment_routes, url_prefix='/api/comments')
app.register_blueprint(alchemy_routes, url_prefix='/api/alchemy')
app.register_blueprint(post_routes, url_prefix='/api/posts')
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)


# Since we are deploying with Docker and Flask,
# we won't be using a buildpack when we deploy to Heroku.
# Therefore, we need to make sure that in production any
# request made over http is redirected to https.
# Well.........
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = { rule.rule: [[ method for method in rule.methods if method in acceptable_methods ],
                    app.view_functions[rule.endpoint].__doc__ ]
                    for rule in app.url_map.iter_rules() if rule.endpoint != 'static' }
    return route_list


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    # return app.send_static_file('index.html')
  # Adjust 'frontend_build' to your actual React/Vite build folder path
    if path != "" and os.path.exists(os.path.join('../react-vite/dist', path)):
        return send_from_directory('../react-vite/dist', path)
    else:
        return send_from_directory('../react-vite/dist', 'index.html')


@app.errorhandler(Exception)
def global_handle_error(e):
    if isinstance(e, HTTPException):
        return error_response(e.description, e.code)
    return error_response("An unexpected error occurred. Please try again later.", 500)
