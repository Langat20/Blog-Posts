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



class BlogForm(FlaskForm):
    title = StringField('Blog Title ',validators = [DataRequired()])
    description = TextAreaField('Write your Blog ',validators=[DataRequired()])
    # postedby = StringField('Posted By: ',validators = [DataRequired()])
    date = DateField('Posting Date', validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Post your Comment ',validators=[DataRequired()])
    # madeby = StringField('Made By: ',validators = [DataRequired()])
    dateposted = DateField('Posting Date', validators=[DataRequired()])
    submit = SubmitField('Add Comment')


class UpdateBlog(FlaskForm):
    description = TextAreaField('Update your blog', validators=[DataRequired()])
    submit = SubmitField('Update')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

