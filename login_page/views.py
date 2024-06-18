import flask 
import flask_login
from registration_page.models import User
from home_page.views import render_home_page
# import os
# import json
def render_login_page():
    
    code=False
    if flask_login.current_user.is_authenticated:
        return render_home_page()
    else:
        if flask.request.method == "POST":
            code="--> registration"
            for user in User.query.filter_by(login=flask.request.form['login']):
                if user.password == flask.request.form['password']:
                    flask_login.login_user(user)
                    code=False
            

    return flask.render_template(
        template_name_or_list= "login.html",
        code=code
    )