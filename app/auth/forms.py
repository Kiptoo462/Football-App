from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,ValidationError,BooleanField,TextAreaField,IntegerField
from wtforms.fields.core import IntegerField
from wtforms.validators import Required,Email,EqualTo
from ..models import User



class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[Required()])
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField("Password",validators=[Required(),EqualTo('password_confirm',message="Passwords Dont match!")])
    password_confirm=PasswordField(label="Confirm Password",validators=[Required()])
    submit=SubmitField('Sign Up')
    
    def check_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('The Email is already used')
        
    def check_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("The Username is already in use")
        
class LoginForm(FlaskForm):
    email=StringField('Enter your email address..', validators=[Required(),Email()])
    password=PasswordField('Enter your password..',validators=[Required()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Login')

class UpdateProfile(FlaskForm):
    favourite_team = TextAreaField('Update your profile.',validators = [Required()])
    submit = SubmitField('Submit')