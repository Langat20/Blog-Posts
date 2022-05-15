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



@main.route('/blog/', methods = ["GET","POST"])
@login_required
def postblog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog = Blog(title=blog_form.title.data, description=blog_form.description.data, date=blog_form.date.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('.homepage'))

    return render_template('blog.html', blog_form= blog_form)


@main.route('/homepage')
def homepage():

    '''
    View root page function that returns the index page and its data
    '''
    blog = Blog.query.all()
    return render_template('homepage.html', blog=blog)


@main.route('/commentform/', methods = ["GET","POST"])
@login_required
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comments(comment=form.comment.data, dateposted=form.dateposted.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('.homepage'))

    return render_template('commentform.html',form= form)


@main.route('/commentview/')
@login_required
def viewcomment():

    '''
    View root page function that returns the index page and its data
    '''
    
    comments = Comments.query.all()
    return render_template('commentview.html', comments=comments)




@main.route('/blogupdate/', methods = ["GET","POST"])
@login_required
def blogupdate():
    # blog = Blog.query.filter_by(id).first()
    # if blog is None:
    #     abort(404)
    
    form = UpdateBlog()

    if form.validate_on_submit():
        description = form.description.data

        blog = Blog(description=description)
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.homepage'))

    return render_template('blogupdate.html',form =form)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

