#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """force locale with parameters"""
    locale = request.args.get('locale', None)
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """return a simple template"""
    return render_template('4-index.html')
