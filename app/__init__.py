from flask import Flask
from config import Config
from app.controllers.auth.user import auth

# 创建Flask应用
ap = Flask(__name__)

ap.register_blueprint(auth)

ap.config.from_object(Config)
