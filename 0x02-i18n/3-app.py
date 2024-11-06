#!/usr/bin/env python3
"""3-app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """class configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    return request.accept_languages.best_match(["en", "fr"])


@app.route("/")
def hello():
    """hello route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
