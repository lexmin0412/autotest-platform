from flask import Flask
from config import Config
from app.controllers.auth.user import auth

# 创建Flask应用
pity = Flask(__name__)

pity.register_blueprint(auth)

pity.config.from_object(Config)
