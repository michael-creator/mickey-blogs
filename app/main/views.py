from flask import Flask, render_template
from.import main



@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')