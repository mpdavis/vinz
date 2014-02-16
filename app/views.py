from flask import current_app
from flask import render_template
from flask import send_from_directory


def initialize_view_urls(app):
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/login/', view_func=login)

    # TODO this is a temporary hack-job solution for serving static files
    app.add_url_rule('/styles/<path:filename>', view_func=serve_static)
    app.add_url_rule('/bower_components/<path:filename>', view_func=serve_bower)
    app.add_url_rule('/scripts/<path:filename>', view_func=serve_scripts)
    app.add_url_rule('/fonts/<path:filename>', view_func=serve_fonts)
    app.add_url_rule('/views/<path:filename>', view_func=serve_views)
    app.add_url_rule('/images/<path:filename>', view_func=serve_images)


def index():
    return render_template('index.html')


def login():
    return render_template('login.html')


# TODO this is a temporary hack-job solution for serving static files
def serve_static(filename):
    return send_from_directory(current_app.static_folder + '/styles/', filename)


def serve_bower(filename):
    return send_from_directory(current_app.static_folder + '/bower_components/', filename)


def serve_scripts(filename):
    return send_from_directory(current_app.static_folder + '/scripts/', filename)


def serve_fonts(filename):
    return send_from_directory(current_app.static_folder + '/fonts/', filename)


def serve_views(filename):
    return send_from_directory(current_app.static_folder + '/views/', filename)


def serve_images(filename):
    return send_from_directory(current_app.static_folder + '/images/', filename)
