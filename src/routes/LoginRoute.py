from flask import Blueprint, render_template, request, flash, redirect, url_for, session

login = Blueprint("login_blueprint", __name__)


@login.route("/login", methods=["GET", "POST"])
def loginF():
    return render_template("login.html")
