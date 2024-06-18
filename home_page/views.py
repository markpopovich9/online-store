import flask 
import flask_login
# import os
# import json
def render_home_page():
    # path_json = os.path.abspath(__file__ + "/../static/json/data.json")
    # with open(path_json, encoding= "utf-8") as file:
    #     read_data =  json.load(file)
    code=False
    if flask_login.current_user.is_authenticated:
        code=flask_login.current_user.login
    print(code)
    return flask.render_template(
        template_name_or_list= "home.html", 
        code=code
    )