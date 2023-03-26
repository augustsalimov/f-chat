import uvicorn
from flask import Flask, render_template

from blueprints import FrontendBlueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "hey"
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
    app.register_blueprint(FrontendBlueprint.app)

    return app


'''def main() -> int:
    create_app().run()
    return 0'''


if __name__ == "__main__":
    raise SystemExit(create_app().run(debug=True))

'''if __name__ == "__main__":
    uvicorn.run(
        "main:create_app()",
        host="0.0.0.0",
        port=8080,
    )'''
