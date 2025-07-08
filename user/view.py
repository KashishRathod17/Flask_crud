from flask import render_template,redirect,request
from models.allusers import allusers
from flask_sqlalchemy import SQLAlchemy

def userview():
    userinfo = allusers.query.all()
    return render_template("user_template/userview.html", userinfo=userinfo)

def updateuser(u_id):
    up_user = allusers.query.filter_by(u_id=u_id).first()
    return render_template("user_template/updateuser.html", up_user=up_user)