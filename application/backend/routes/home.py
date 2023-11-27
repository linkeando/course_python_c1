from flask import Blueprint, render_template, request, jsonify

from application.backend.config.database import SQLiteHandler
from application.backend.services.login import LoginService

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET'])
def login_page():
    return render_template("home.html")


@home_bp.route('/', methods=['POST'])
def login():
    return LoginService(request.form['username'], request.form['password']).authenticate()


@home_bp.route('/home/add_user', methods=['POST'])
def test():
    # Ejemplo de uso
    db_name = 'example.db'
    table_name = 'users'
    columns = ['id INTEGER PRIMARY KEY', 'name TEXT', 'age INTEGER']
    data = {'name': 'John Doe', 'age': 25}

    # Crear una instancia de la clase SQLiteHandler
    sqlite_handler = SQLiteHandler(db_name)

    # Crear la tabla si no existe
    sqlite_handler.create_table(table_name, columns)

    # Insertar datos en la tabla
    sqlite_handler.insert_data(table_name, data)

    # Cerrar la conexión
    sqlite_handler.close_connection()
    json: dict = request.get_json()
    error_result = {'message': 'Mensaje enviado desde python'}
    return jsonify(error_result), 201


def init_app(app):
    app.register_blueprint(home_bp)
