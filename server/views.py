from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask.ext.login import login_required

from internal.auth import get_current_user
from internal.auth import login_user
from internal.auth import logout_user
from internal.auth import utils as auth_utils

import urllib


def initialize_view_urls(app):
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/login/', view_func=login, methods=['GET', 'POST'])
    app.add_url_rule('/logout/', view_func=logout)


@login_required
def index():
    g.user = get_current_user()
    return render_template('index.html')


def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        # Get the user
        user = auth_utils.maybe_get_user_by_email(email)
        if user:
            # If the user exists, check their password
            authenticated = user.check_password(password)
            if authenticated:
                # User is legit, give them a session.
                login_user(user)

                redirect_location = request.args.get('redirect')
                if redirect_location:
                    return redirect(urllib.unquote(redirect_location))
                return redirect(url_for('index'))

        # In case any of the conditionals fail, show the error on the login page.
        g.incorrect = True
        g.email = email
    return render_template('login.html')


def logout():
    logout_user()
    return redirect(url_for('login'))
