from flask import abort, redirect, render_template, url_for, flash

from app.requests import get_random_quote
from .. import db
from ..models import Blog, Comments, Subscribe,User
from ..email import mail_message
from .forms import BlogForm, CommentForm, SubscribedUserForm, UpdateBlog, UpdateProfile
from . import main
from flask_login import login_required


@main.route('/', methods = ["GET","POST"])
def index():

    quotes = get_random_quote()

    form = SubscribedUserForm()
    if form.validate_on_submit():
        subscribe = Subscribe(email = form.email.data)
        # db.session.add(subscribe)
        # db.session.commit()
        subscribe.save_subscriber()
        form.email.data = ""
        mail_message("Welcome to bloglist","email/subscribe",subscribe.email,user=subscribe)

        flash("Your Subscription is successful")
        

        return redirect(url_for('main.index'))

    return render_template('index.html', subform = form, quotes=quotes)



