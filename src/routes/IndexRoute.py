from flask import Blueprint, render_template, session, flash


index = Blueprint("index_blueprint", __name__)


@index.route("/")
def home():
    return render_template("index.html")
