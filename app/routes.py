import base64

from flask import Blueprint, render_template, request

from .config import ALLOWED_EXTENSIONS
from .model_service import predict_image

main_bp = Blueprint("main", __name__)


def _is_allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@main_bp.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    image_data_url = None

    if request.method == "POST":
        uploaded = request.files.get("image")

        if not uploaded or uploaded.filename == "":
            error = "Please choose an image file."
        elif not _is_allowed_file(uploaded.filename):
            error = "Allowed file types: png, jpg, jpeg, webp."
        else:
            file_bytes = uploaded.read()
            if not file_bytes:
                error = "Uploaded file is empty."
            else:
                mime = uploaded.mimetype or "image/jpeg"
                b64 = base64.b64encode(file_bytes).decode("utf-8")
                image_data_url = f"data:{mime};base64,{b64}"

                try:
                    result = predict_image(file_bytes)
                except Exception as exc:
                    error = f"Prediction failed: {exc}"

    return render_template(
        "index.html",
        result=result,
        error=error,
        image_data_url=image_data_url,
    )
