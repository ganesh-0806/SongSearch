from flask import Flask
import os
import yaml
from pymongo import MongoClient
from .models import User

db_file_path = os.path.join(os.path.dirname(__file__), 'db.yml')
db_config = yaml.full_load(open(db_file_path))
client = MongoClient()
client = MongoClient('mongodb://'+db_config['host']+':'+db_config['port']+'/')
db = client.testdb
user = User()

def create_app():
    app = Flask(__name__)

    from .views import views
    from .playlist import playlist
    from .auth import auth
    
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(playlist, url_prefix='/')

    return app
