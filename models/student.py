from dbconnection import db

class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(100), nullable=False)
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    per = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'{self.s_id} - {self.s_name}'
