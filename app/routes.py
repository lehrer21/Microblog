from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dennis'}
    posts = [
        {
            'author': {'username': 'Tom'},
            'body': 'Beautiful day in Chicago!'
        },
        {
            'author': {'username': 'Patrick'},
            'body': 'The Chappie movie is perfect.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)