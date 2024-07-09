from flask import Blueprint, render_template, session, flash


cursos = Blueprint("cursos_blueprint", __name__)


@cursos.route("/")
def home():
    return render_template("cursos.html")
