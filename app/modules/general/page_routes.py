from flask import render_template
from . import general_bp

@general_bp.route('/')
def index():
    return render_template('index.html') 


@general_bp.route('/articles')
def about():
    return render_template('articles.html')



@general_bp.route('/contact')
def contact():
    return render_template('contact.html')  