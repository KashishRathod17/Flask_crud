from dbconnection import db
# import dbconnection

class allusers(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    p_no = db.Column(db.String(10), nullable=False)
    b_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"{self.u_id} - {self.name}"
    
    def to_dict(self):
        return { 
            'u_id':self.u_id,
            'email':self.email,
            'name':self.name,
            'p_no':self.p_no,
            'b_date':self.b_date.strftime('%Y-%m-%d') 
        }