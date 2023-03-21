import flask

from flask import Flask, render_template, flash, redirect, url_for

from forms import RegistrationForm

# from db import User, db


class FrontendBlueprint:
    app = flask.Blueprint("frontend", __name__, template_folder="../templates")

    @staticmethod
    @app.route("/", methods=["GET"])
    def get_main_page():
        reg_form = RegistrationForm()

        return render_template("index.html", form=reg_form)

    @staticmethod
    @app.route("/", methods=["POST"])
    def post_reg_data():
        reg_form = RegistrationForm()
        if reg_form.validate_on_submit():
            """username = reg_form.username.data
            password = reg_form.password.data

            user_object = User.query.filter_by(username=username).first()
            if user_object:
                return "Someone else has taken this username"

            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()

            flash('Registered successfully. Please login.', 'success')
            return redirect(url_for('login'))"""
            return "Great success"

        return render_template("index.html", form=reg_form)
