from flask import Blueprint
from student.view import studentview,updatestudent,deletestudent

bp = Blueprint('student',__name__)

bp.add_url_rule('/studentview',view_func=studentview,endpoint='studentview',methods=['GET','POST'])
bp.add_url_rule('/updatestudent/<int:s_id>',view_func=updatestudent,endpoint='updatestudent',methods=['GET','POST'])
bp.add_url_rule('/deletestudent/<int:s_id>',view_func=deletestudent,endpoint='deletestudent',methods=['GET','POST'])

