from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired,Email
from ..models import User
from wtforms import ValidationError



class SubscribedUserForm(FlaskForm):
    email = StringField('Your Email Address to subscribe to our daily Updates',validators=[DataRequired(),Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('Email Already subscribed')




