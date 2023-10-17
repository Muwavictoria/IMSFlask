from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError
from app import models



class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min=6, max=20)], render_kw={"placeholder" : "Username", "class" : "form-control"})

    password = PasswordField(validators=[InputRequired(),Length(min=6, max=20)], render_kw={"placeholder" : "Password" , "class" : "form-control"})

    submit = SubmitField('Register',  render_kw={"class" : "form-control"})

    def validate_username(self, username):
        existing_username = models.User.query.filter_by(username=username.data).first()

        if existing_username:
            raise ValidationError(
                "That username already exits. Please choose a different one"
            )
       

class LoginForm(FlaskForm):
   username = StringField(validators=[InputRequired(),Length(min=6, max=20)], render_kw={"placeholder" : "Username", "class" : "form-control"})
   password = PasswordField(validators=[InputRequired(),Length(min=6, max=20)], render_kw={"placeholder" : "Password" , "class" : "form-control"})
   submit = SubmitField('Login',  render_kw={"class" : "form-control"})

