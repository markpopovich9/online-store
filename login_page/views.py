import flask 
import flask_login
from registration_page.models import User

# import os
# import json
def render_login_page():
    if flask_login.current_user.is_authenticated:
        print("Hello World")
    else:
        if flask.request.method == "POST":
            for user in User.query.filter_by(login=flask.request.form['login']):
                if user.password == flask.request.form['password']:
                    flask_login.login_user(user)
    return flask.render_template(
        template_name_or_list= "login.html"
    )