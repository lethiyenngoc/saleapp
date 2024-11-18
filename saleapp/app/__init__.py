from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from urllib.parse import quote
from flask_login import LoginManager
import cloudinary
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.secret_key = 'HJGGHD*^&R$YGFGHDYTRER&*TRTYCHG^R&^T'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Admin123@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 7

db = SQLAlchemy(app)
login = LoginManager(app)

cloudinary.config(
    cloud_name="dn8ek8zvk",
    api_key="244914198474198",
    api_secret="5NrnclAXw7-nBut52xZ8lWk14S0",
    secure=True
)
