from flask import Blueprint, jsonify, request
from app.models import db, ContentSource
from app.utils import validate_url, error_response, success_response

content_source_routes = Blueprint("content_sources", __name__)

# Helper function to fetch content source
def fetch_content_source(id):
    source = ContentSource.query.get(id)
    if not source:
        return error_response("🥲 That creative content can't be found. Please try again.", 404)
    return source

# GET ROUTES

@content_source_routes.route("/feed", methods=["GET"])
def get_feed():
    try:
        page = int(request.args.get("page", 1))
        each_page = int(request.args.get("each_page", 10))
        if page < 1 or each_page < 1:
            raise ValueError
    except ValueError:
        page, each_page = 1, 10  # Default to valid values

    sources = ContentSource.query.paginate(page=page, per_page=each_page, error_out=False)
    return success_response(
        "Feed retrieved successfully! 🤗",
        {
            "sources": [source.to_dict() for source in sources.items],
            "page": sources.page,
            "each_page": each_page,
            "total_pages": sources.pages,
        },
    )


@content_source_routes.route("/<int:id>", methods=["GET"])
def get_source(id):
    source = ContentSource.query.get(id)
    if not source:
        return error_response("🥲 That creative content can't be found. Please try again.", 404)

    source.glances += 1
    db.session.commit()

    return success_response("Source retrieved successfully 🤗", {
        "id": source.id,
        "name": source.name,
        "media_type": source.source_type,
        "summary": "Preview"
    })
@content_source_routes.route("/search", methods=["GET"])
def search_sources():
    search = request.args.get("search", "")
    source_filter = request.args.get("type", "")

    
    try:
        page = int(request.args.get("page", 1))
        if page <= 0:
            raise ValueError
    except ValueError:
        page = 1

    try:
        each_page = int(request.args.get("each_page", 10))
        if each_page <= 0:
            raise ValueError
    except ValueError:
        each_page = 10


    query = ContentSource.query


    if search:
        query = query.filter(ContentSource.name.ilike(f"%{search}%"))
    if source_filter:
        query = query.filter(ContentSource.source_type == source_filter)

    # Pagination
    sources = query.paginate(page=page, per_page=each_page, error_out=False)


    if not sources.items:
        return success_response("No sources match your search criteria.", {
            "sources": [],
            "total_pages": 0,
            "page": page,
            "each_page": each_page
        })

    # Return paginated results
    return success_response("Sources retrieved successfully🤗", {
        "sources": [source.to_dict() for source in sources.items],
        "total_pages": sources.pages,
        "page": sources.page,
        "each_page": each_page
    })


# POST ROUTES

@content_source_routes.route("/", methods=["POST"])
def create_source():
    data = request.get_json()

    if not data or not all([data.get("name"), data.get("type"), data.get("url")]):
        return error_response("🥲 Missing required fields.", 400)

    # Validate the URL
    try:
        validate_url(data.get("url"))
    except ValueError as e:
        return error_response(str(e), 400)

    # Create the new content source
    new_source = ContentSource(
        name=data.get("name"),
        source_type=data.get("type"),
        url=data.get("url")
    )
    db.session.add(new_source)
    db.session.commit()

    return success_response("Source created successfully🤗", new_source.to_dict(), 201)
    # data = request.get_json()

    # # Check for missing fields
    # required_fields = ["name", "type", "url"]
    # missing = [field for field in required_fields if not data.get(field)]
    # if missing:
    #     return error_response(f"🥲 Missing required fields: {', '.join(missing)}", 400)

    # # Validate URL format
    # if not validate_url.url(data["url"]):
    #     return error_response("🤖 The URL provided is invalid.", 400)

    # new_source = ContentSource(
    #     name=data["name"],
    #     source_type=data["type"],
    #     url=data["url"]
    # )
    # db.session.add(new_source)
    # db.session.commit()
    # try:
    #     return success_response("Source created successfully🤗", new_source.to_dict(), 201)
    # except Exception as e:
    #     db.session.rollback()
    #     return error_response(f"Error serializing response: {str(e)}", 500)

@content_source_routes.route("/<int:id>/like", methods=["POST"])
def like_source(id):
    source = ContentSource.query.get(id)
    if not source:
        return error_response("🥲 That creative content can't be found. Please try again.", 404)

    source.elixirs += 1
    db.session.commit()
    return success_response("Elixir added!🔮", {"total_elixirs": source.elixirs})

@content_source_routes.route("/<int:id>/share", methods=["POST"])
def share_source(id):
    source = ContentSource.query.get(id)
    if not source:
        return error_response("🥲 That creative content can't be found. Please try again.", 404)

    source.transmutations += 1
    db.session.commit()
    return success_response("🔄Content transmuted!🛸", {"total_transmutations": source.transmutations})

# PUT ROUTES

@content_source_routes.route("/<int:id>", methods=["PUT"])
def update_source(id):
    source = ContentSource.query.get(id)
    if not source:
        return error_response("🥲 That creative content can't be found. Please try again.", 404)

    data = request.get_json()
    if not data:
        return error_response("🥲 Please provide valid data.", 400)

    if "url" in data:
        try:
            validate_url(data.get("url"))
        except ValueError as e:
            return error_response(str(e), 400)

    source.name = data.get("name", source.name)
    source.source_type = data.get("type", source.source_type)
    source.url = data.get("url", source.url)
    db.session.commit()

    return success_response("Source updated successfully 🤗", source.to_dict())



# DELETE ROUTES

@content_source_routes.route("/<int:id>", methods=["DELETE"])
def delete_source(id):
    source = fetch_content_source(id)
    if isinstance(source, dict):
        return source

    db.session.delete(source)
    db.session.commit()
    return success_response("Creation Deleted Successfully 🤞🏾")
