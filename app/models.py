from datetime import datetime
from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    blogs= db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship("Comments", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user(cls, id):
        pitches= User.query.filter_by(id=id).all()
        return pitches


    def __repr__(self):
        return f'User{self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(5555))
    # postedby = db.Column(db.String(255))

    date = db.Column(db.DateTime,default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments= db.relationship('Comments', backref='blog', lazy='dynamic')


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, id):
        pitches= Blog.query.filter_by(id=id).all()
        return pitches

    def __repr__(self):
        return f'User {self.name}'


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    # madeby = db.Column(db.String(255))
    dateposted = db.Column(db.Date)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        pitches= Comments.query.filter_by(id=id).all()
        return pitches

    def __repr__(self):
        return f'User {self.name}'


class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    email = db.Column(db.String(255),unique = True,index = True)


    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    

    @classmethod
    def get_subscriber(cls, id):
        pitches= Subscribe.query.filter_by(id=id).all()
        return pitches

    def __repr__(self):
        return f'User {self.name}'

class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote



