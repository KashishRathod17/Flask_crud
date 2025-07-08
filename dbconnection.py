from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()
 
def init_app(app):
    db.init_app(app)