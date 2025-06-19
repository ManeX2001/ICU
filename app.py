from flask import Flask
from config import Config
from routes.main import main as main_blueprint
from routes.api  import api  as api_blueprint

def create_app():
    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )
    app.config.from_object(Config)

    # register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    print('🚀 Flask app running at http://127.0.0.1:5000')
    app.run(host='0.0.0.0', port=5000, debug=True)