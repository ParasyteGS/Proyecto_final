from flask import Flask
from .routes import IndexRoute, LoginRoute, CursosRoute


def create_app():
    app = Flask(__name__)

    app.register_blueprint(LoginRoute.login)
    app.register_blueprint(IndexRoute.index)
    app.register_blueprint(CursosRoute.cursos, url_prefix="/cursos")

    return app
