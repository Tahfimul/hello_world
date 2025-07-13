from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField

class NewUserForm(FlaskForm):
    first_name = StringField(label='First Name')
    last_name = StringField(label='Last Name')
    email_address = StringField(label='Email Address')
    phone_number = TelField(label='Phone Number')
    activate_submit_btn = SubmitField(label='Activate Account')
