from pathlib import Path

from flask import Flask

from .routes import main_bp


def create_app() -> Flask:
    root_dir = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=str(root_dir / "templates"),
        static_folder=str(root_dir / "static"),
    )
    app.register_blueprint(main_bp)
    return app
