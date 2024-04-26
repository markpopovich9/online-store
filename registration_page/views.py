import flask 
# import os
# import json
def render_reg_page():
    # path_json = os.path.abspath(__file__ + "/../static/json/data.json")
    # with open(path_json, encoding= "utf-8") as file:
    #     read_data =  json.load(file)
    
    return flask.render_template(
        template_name_or_list= "reg.html"
    )