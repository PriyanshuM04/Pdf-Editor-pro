ALLOWED_EXTENSIONS = {"pdf"}

def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def api_response(success, message, data=None):
    response = {
        "success": success,
        "message": message
    }
    if data is not None:
        response["data"] = data
    return response
