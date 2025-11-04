from flask import Flask
def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_mapping(SECRET_KEY="change_me_here")
    from .routes import main
    app.register_blueprint(main)
    return app
