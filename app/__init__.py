from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Register blueprints
    from app.routes.pdf_routes import pdf_bp
    app.register_blueprint(pdf_bp)

    # Global error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "error": str(e)
        }), 500

    return app
