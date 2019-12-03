from flask import render_template,request,redirect,url_for,abort
from ..models import User
from.import main
from flask_login import login_required
from app.request import GetQuotes
from .forms import UpdateProfile
from .. import db

@main.route('/')
def index():
    quotes = GetQuotes()
    print(quotes)
    return render_template('index.html',quotes=quotes)

@main.route('/about',methods = ['GET','POST'])
def about():
    return render_template('about.html')


@main.route('/contact',methods = ['GET','POST'])
def contact():
        
    return render_template('contact.html')


@main.route('/new_review',methods = ['GET','POST'])
def new_review():
 
    return render_template('new_review.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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