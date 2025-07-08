from flask import render_template,redirect,request
from models.student import Student
from dbconnection import db
from flask_sqlalchemy import SQLAlchemy

def studentview():
    if request.method=='POST':
        s_name = request.form['s_name']
        sub1 = request.form['sub1']
        sub2 = request.form['sub2']
        sub3 = request.form['sub3']
        st = Student(s_name=s_name,sub1=sub1,sub2=sub2,sub3=sub3)
        db.session.add(st)
        db.session.commit()
    studentinfo = Student.query.all()
    return render_template('student_template/studentview.html',studentinfo=studentinfo)

def updatestudent(s_id):
    if request.method == 'POST':
        s_name = request.form['s_name']
        sub1 = request.form['sub1']
        sub2 = request.form['sub2']
        sub3 = request.form['sub3']
        up_st = Student.query.filter_by(s_id=s_id).first()
        up_st.s_name = s_name
        up_st.sub1 = sub1
        up_st.sub2 = sub2
        up_st.sub3 = sub3
        db.session.add(up_st)
        db.session.commit()
        return redirect('/studentview')
    up_st = Student.query.filter_by(s_id=s_id).first()
    return render_template('student_template/updatestudent.html',up_st=up_st)

def deletestudent(s_id):
    d_st = Student.query.filter_by(s_id=s_id).first()
    db.session.delete(d_st)
    db.session.commit()
    return redirect('/studentview')

    