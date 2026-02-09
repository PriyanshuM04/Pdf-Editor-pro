from flask import Blueprint, request, jsonify
from app.services.pdf_editor import merge_pdfs
from app.utils.file_handler import api_response

pdf_bp = Blueprint("pdf", __name__)

@pdf_bp.route("/merge", methods=["POST"])
def merge_pdf():
    files = request.files.getlist("files")

    if not files or len(files) < 2:
        return jsonify(
            api_response(
                False,
                "At least two PDF files are required"
            )
        ), 400

    output_file = merge_pdfs(files)

    return jsonify(
        api_response(
            True,
            "PDFs merged successfully",
            {"output_file": output_file}
        )
    ), 200
