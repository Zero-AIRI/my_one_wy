from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
db = SQLAlchemy()
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/house"
    SQLALCHEMY_TRACK_MODIFICATIONS = True