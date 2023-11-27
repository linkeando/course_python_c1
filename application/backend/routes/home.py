from flask import Blueprint, render_template, request

from application.backend.services.login import LoginService

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET'])
def login_page():
    return render_template("home.html")


@home_bp.route('/', methods=['POST'])
def login():
    return LoginService(request.form['username'], request.form['password']).authenticate()


def init_app(app):
    app.register_blueprint(home_bp)
