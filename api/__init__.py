from flask import Blueprint
from api.allusers_api import userjson,getuser,getalluser,apideleteuser,updateuserapi

bp = Blueprint('api',__name__,url_prefix='/api')

bp.add_url_rule('/userjson',view_func=userjson,endpoint='userjson',methods=['POST'])
bp.add_url_rule('/getuser/<int:u_id>',view_func=getuser,endpoint='getuser',methods=['GET'])
bp.add_url_rule('/getalluser',view_func=getalluser,endpoint='getalluser',methods=['GET'])
bp.add_url_rule('/apideleteuser/<int:u_id>',view_func=apideleteuser,endpoint='apideleteuser',methods=['DELETE'])
bp.add_url_rule('/updateuserapi/<int:u_id>',view_func=updateuserapi,endpoint='updateuserapi',methods=['PUT'])