from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__="users"
    
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),index=True)
    email= db.Column(db.String(50),unique=True,index=True)
    encryptedpassword= db.Column(db.String(200),index=True)
    
    @property
    def password(self):
        raise AttributeError ("Encrypted!")
    
    @password.setter
    def password(self,password):
        self.encryptedpassword= generate_password_hash(password)
        
    def passwordVerification(self,password):
        return check_password_hash(self.encryptedpassword,password)

    def __repr__(self):
        return f'User{self.username}'