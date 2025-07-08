from flask import Blueprint
from user.view import userview,updateuser

bp = Blueprint('user',__name__)
bp.add_url_rule('/',view_func=userview,endpoint='index',methods=['GET','POST'])
bp.add_url_rule('/updateuser/<int:u_id>',view_func=updateuser,endpoint='update',methods=['GET','POST'])
# bp.add_url_rule('/deleteuser/<int:u_id>',view_func=deleteuser,endpoint='delete',methods=['GET','POST'])