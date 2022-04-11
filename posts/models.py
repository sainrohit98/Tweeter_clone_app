from extentions import db
from datetime import datetime
from geoalchemy2 import Geometry


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250))
    location = db.Column(Geometry('POINT'))
    timestamp = db.Column(db.DateTime,default=datetime.now(),nullable = False)

    def __repr__(self):
        return '<post %r>' % self.id