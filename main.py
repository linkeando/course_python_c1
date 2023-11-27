from waitress import serve

from application.backend.config.route_manager import RouteManager
from application.flask_app import FlaskApp

app = FlaskApp().create_app()
route_manager = RouteManager(app, "application.backend.routes").register_routes()

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    #serve(app, host='0.0.0.0', port=3000)
