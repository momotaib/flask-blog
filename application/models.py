from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Posts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(3000), unique=True)
    title=db.Column(db.String(100), unique=True)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join(['User ID: ', self.user_id, '\r\n', 'Title: ', self.title, '\r\n', self.content])

class Users(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150), nullable=False, unique=True) 
    password=db.Column(db.String(128), nullable=False)
    first_name=db.Column(db.String(30), nullable=False)
    last_name=db.Column(db.String(30), nullable=False)
    posts=db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n', 
        'Email: ', self.email, '\r\n',
        'Name: ', self.first_name, ' ', self.last_name])



