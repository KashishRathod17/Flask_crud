from flask import render_template,redirect,request
from models.allusers import allusers
from dbconnection import db
from flask_sqlalchemy import SQLAlchemy

# @user.route('/', methods =['GET','POST'])
def userview():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     email = request.form['email']
    #     p_no = request.form['p_no']
    #     b_date = request.form['b_date']
    #     uv = allusers(name=name,email=email,p_no=p_no,b_date=b_date)
    #     db.session.add(uv)
    #     db.session.commit()
    userinfo = allusers.query.all()
    return render_template("user_template/userview.html", userinfo=userinfo)

def updateuser(u_id):
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         p_no = request.form['p_no']
#         b_date = request.form['b_date']
#         up_user = allusers.query.filter_by(u_id=u_id).first()
#         up_user.name = name
#         up_user.email = email
#         up_user.p_no = p_no
#         up_user.b_date = b_date
#         db.session.add(up_user)
#         db.session.commit()
#         return redirect('/')
    up_user = allusers.query.filter_by(u_id=u_id).first()
    return render_template("user_template/updateuser.html", up_user=up_user)

# def deleteuser(u_id):
#     d_user = allusers.query.filter_by(u_id=u_id).first()
#     db.session.delete(d_user)
#     db.session.commit()
#     return redirect('/')