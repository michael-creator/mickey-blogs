from flask import Flask, render_template
from.import main
from flask_login import login_required



@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/about',methods = ['GET','POST'])
def about():
    return render_template('about.html')


@main.route('/contact',methods = ['GET','POST'])
def contact():
        
    return render_template('contact.html')


@main.route('/new_review',methods = ['GET','POST'])
def new_review():
 
    return render_template('new_review.html')