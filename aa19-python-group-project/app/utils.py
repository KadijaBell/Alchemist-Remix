from flask import jsonify

def get_content_source_or_404(id, model):
    source = model.query.get(id)
    if not source:
        return {"error": "🥲 That creative content can't be found. Please try again."}, 404
    return source

def success_response(message, data=None):
    response = {"message": message}
    if data:
        response["data"] = data
    return jsonify(response), 200

def error_response(message, status_code, details=None):
    response = {
        "error": {
            "message": message,
            "status_code": status_code
        }
    }
    if details:
        response["error"]["details"] = details
    return jsonify(response), status_code


def validate_data(data, required_fields):
   missing_data = [field for field in required_fields if field not in data]
   if missing_data:
       return error_response(f"🥲 Missing required fields: {', '.join(missing_data)}", 400)
   return None

def validate_error_response(error):
    return {"error": "Validation failed", "details": error}, 400
