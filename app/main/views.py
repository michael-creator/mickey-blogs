from flask import Flask, render_template
from.import main


def index():
    return render_template(index.html)
@main.route('/')
def index():
    
    return render_template('index.html')