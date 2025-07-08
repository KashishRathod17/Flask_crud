from flask import jsonify, request
from models.allusers import allusers
from dbconnection import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# post api
def userjson():
    data = request.get_json()
    # print(data)
    try:
        alluser = allusers(
            email=data["email"],
            name=data["name"],
            p_no=data["p_no"],
            b_date=datetime.strptime(data["b_date"], "%Y-%m-%d"),
        )
        db.session.add(alluser)
        db.session.commit()
        # print(alluser)
        return jsonify({"message": "User created", "user id": alluser.u_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# get api for single user
def getuser(u_id):
    try:
        user = allusers.query.get(u_id)
        result = {
            "u_id": user.u_id,
            "email": user.email,
            "name": user.name,
            "p_no": user.p_no,
            "b_date": user.b_date,
        }
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# get api for all users
def getalluser():
    try:
        users = allusers.query.all()
        result = [user.to_dict() for user in users]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# delete user api
def apideleteuser(u_id):
    try:
        d_user = allusers.query.filter_by(u_id=u_id).first()
        db.session.delete(d_user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# update user api 
def updateuserapi(u_id):
    try:
        user = allusers.query.filter_by(u_id=u_id).first()
        data = request.get_json()
        user.email = data["email"]
        user.name = data["name"]
        user.p_no = data["p_no"]
        user.b_date = data["b_date"]
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
