import flask 
import flask_sqlalchemy, flask_migrate
import os

shop = flask.Flask(
    import_name= "settings",
    instance_path=   os.path.abspath(__file__ + "/.."),
    template_folder= "project/templates"
)
shop.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
DATABASE  = flask_sqlalchemy.SQLAlchemy(app=shop)
MIGRATE = flask_migrate.Migrate(app=shop , db= DATABASE)