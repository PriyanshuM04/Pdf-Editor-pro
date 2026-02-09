from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from app.routes.pdf_routes import pdf_bp
    app.register_blueprint(pdf_bp)

    return app
