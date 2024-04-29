import flask 
import flask_login
from .models import User
from project.settings import DATABASE
# import os
# import json
def render_reg_page():
    # path_json = os.path.abspath(__file__ + "/../static/json/data.json")
    # with open(path_json, encoding= "utf-8") as file:
    #     read_data =  json.load(file)
    code  = False
    # if flask_login.current_user.is_authenticated:
        
    if flask.request.method == "POST":
        print(flask.request.form)
    
        if flask.request.form['password'] == flask.request.form['Password_confirmation']:
            

            user = User(
                login = flask.request.form['login'],
                email = flask.request.form['email'],
                password = flask.request.form['password']
            )

            try:
                DATABASE.session.add(user)
                DATABASE.session.commit()
                code = "--> authorization"
            except:
                return "ERROR"
    return flask.render_template(
        template_name_or_list= "reg.html",
        code =  code
    )