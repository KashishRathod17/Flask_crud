from flask import Flask
from dbconnection import db 
import dbconnection
from config import Config
from user import bp as USER_Blueprint
from student import bp as STUDENT_Blueprint
from api import bp as API
from models.allusers import allusers
from models.student import Student

# Creates the Flask application object.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = Config.SQLALCHEMY_ECHO

dbconnection.init_app(app)
app.register_blueprint(USER_Blueprint)
app.register_blueprint(STUDENT_Blueprint)
app.register_blueprint(API)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # print('database created!')
    app.run(debug=True)

# for error issues before activate the environment
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass