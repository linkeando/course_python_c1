import os

from flask import Flask


class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.init_sessions()

    def init_sessions(self):
        self.app.static_folder = os.path.join(os.path.dirname(__file__), 'frontend', 'static')
        self.app.template_folder = os.path.join(os.path.dirname(__file__), 'frontend', 'templates')

    def create_app(self):
        return self.app
