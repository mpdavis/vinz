from flask import render_template


def initialize_view_urls(app):
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/login/', view_func=login)


def index():
    return render_template('index.html')


def login():
    return render_template('login.html')
