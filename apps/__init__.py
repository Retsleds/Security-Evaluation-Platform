from flask import Flask
import settings
from apps.index.view import index_bp
from apps.task.view import task_bp
from apps.nmap.view import nmap_bp

from .extensions import mongo

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)

    mongo.init_app(app)
    app.register_blueprint(index_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(nmap_bp)

    print('##', app.url_map)

    return app