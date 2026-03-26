from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired, InputRequired, Regexp, Email, Length


class ValidationForm(Form):
    email = StringField('email', validators=[InputRequired(), Email()])
    name = StringField('name', validators=[InputRequired(), Length(min=3, max=25)])
    password = PasswordField('pass', validators=[InputRequired(), Length(min=8, message='Password must be 8 characters!'), Regexp(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', message="Password must contain at least one lowercase letter, one uppercase letter, and one digit")])
    
    phone = StringField('phone')

