import flask 
import os

shop = flask.Flask(
    import_name="settings",
    instance_path=   os.path.abspath(__file__ + "/.."),
    template_folder= "project/templates"
)