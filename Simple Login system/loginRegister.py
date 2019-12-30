from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo,Regexp
from tables import User
from werkzeug.security import  check_password_hash
import main


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', 
    	                   validators=[DataRequired(), Length(min=8, max=25), 
    	                   Regexp(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[!#$%&@*])[a-zA-Z0-9!#$%&@*]{8,}', message=('Your password must meet these requirements: At least one DIGIT, At least one UPPERCASE letter, At least one LOWERCASE letter, At least one SPECIAL character[!#$%&@*]'))])
    
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    agree = BooleanField('I agree to terms and conditions',
    					validators=[DataRequired()])
    
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Sorry, this username is taken.')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(max=20)])
    
    password = PasswordField('Password', 
                            validators=[DataRequired(), Length(max=25)])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user is None:
            raise ValidationError('Invalid username.')

    def validate_password(self, password):

        user = User.query.filter_by(username=self.username.data).first()

        if (user is not None):            
            
            password = main.bcrypt.check_password_hash(user.password_hash, password.data)

            if password is False:
                raise ValidationError('Invalid password.')