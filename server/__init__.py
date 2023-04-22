from flask import Flask
import os
import yaml
from pymongo import MongoClient

db_file_path = os.path.join(os.path.dirname(__file__), 'db.yml')
db_config = yaml.full_load(open(db_file_path))
client = MongoClient()
client = MongoClient('mongodb://'+db_config['host']+':'+db_config['port']+'/')
db = client.testdb

def create_app():
    app = Flask(__name__)

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')

    return app
