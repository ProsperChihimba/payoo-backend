import logging
from flask import Flask, jsonify
from config.config import ProductionConfig, TestingConfig, DevelopmentConfig
from utils.database import db
from routes.airtime import airtime_routes, webhook
from flask_cors import CORS, cross_origin


app = Flask(__name__)

#cheaking the enviroment the application is running
if app.config["ENV"] == "production":
    app_config = ProductionConfig
elif app.config["ENV"] == "testing":
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)


CORS(airtime_routes)
CORS(webhook)

#registering api endpoints routes in blueprint from routes directory
app.register_blueprint(airtime_routes, url_prefix='/airtime')
app.register_blueprint(webhook, url_prefix='/webhook')



db.init_app(app)
with app.app_context():
    db.create_all()
