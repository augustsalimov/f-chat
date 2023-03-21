import flask

from flask import Flask, render_template

from fields import *
from models import *

class IndexBlueprint:
    app = flask.Blueprint("index", __name__, template_folder="../templates")

    @staticmethod
    @app.route("/", methods=["GET", "POST"])
    def index():
        reg_form = RegistrationForm()
        if reg_form.validate_on_submit():
            return "Great success"

        return render_template("index.html", form=reg_form)
