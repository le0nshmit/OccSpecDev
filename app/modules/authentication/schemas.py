from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import InputRequired, Email, Length, Regexp

class ValidationForm(Form):
    '''Validation for register form'''

    name_min, name_max = 3, 25
    pass_min = 8
    
    email = StringField('email', validators=[InputRequired(), Email()])
    name = StringField('name', validators=[InputRequired(), Length(min=3, max=25, message=f'Must be {name_min}-{name_max} characters!')])
    password = PasswordField('pass', validators=[InputRequired(), Length(min=8, message=f'Must be atleast {pass_min} characters!'), Regexp(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', message="Must contain at least one lowercase, uppercase letter and atleaest one digit!")])

    type = StringField('type')
    phone = StringField('phone')