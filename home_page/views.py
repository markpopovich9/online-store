import flask 
import flask_login
# import os
# import json
def render_home_page():
    try:
        count =  len(flask.request.cookies.get('products').split(" ")) # python + flask get
        if flask.request.cookies.get('products').split(" ")[0]== "":
            count = "0"
    except:
        count = "0"
    # path_json = os.path.abspath(__file__ + "/../static/json/data.json")
    # with open(path_json, encoding= "utf-8") as file:
    #     read_data =  json.load(file)
    code=False
    if flask_login.current_user.is_authenticated:
        code=flask_login.current_user.login
    print(code)
    return flask.render_template(
        template_name_or_list= "home.html", 
<<<<<<< HEAD
        code=code
=======
        code=code,
        count=count
>>>>>>> b07282d09d6117d19b2de2fc16bd5bdf8f4d896f
    )