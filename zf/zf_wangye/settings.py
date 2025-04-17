from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
db = SQLAlchemy()

class Config:
    DEBUUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/house"
