from flask import render_template,redirect, url_for, flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from flask_login import login_required, login_user, logout_user
from .. import db
from ..email import mail_message


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Blogposts","email/welcome_user",user.email,user=user)

        flash("Account created Successfully")

        return redirect(url_for('auth.login'))

        
    return render_template('auth/register.html',registration_form = form)






    