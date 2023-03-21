from flask import Flask, render_template

from fields import *
from models import *
from blueprints import IndexBlueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "hey"
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
    app.register_blueprint(IndexBlueprint.app)
    
    return app


def main() -> int:
    create_app().run(debug=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
