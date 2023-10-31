#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, request, g, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('5-app.Config')


@babel.localeselector
def get_locale():
    """force locale with parameters"""
    locale = request.args.get('locale', None)
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """returns a user dictionary or none if id is not found"""
    login_as = request.args.get("login_as", None)
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """find a user if any and set it as global on flask.g.user"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """return a simple template"""
    return render_template('5-index.html')
