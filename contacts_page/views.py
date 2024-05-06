import flask
import flask_login
from registration_page.models import User, Product

def render_contacts_page():
    products = {}
    print(User.query.all(),type(User.query.all()))
    
    return flask.render_template(template_name_or_list="contacts.html",name=flask_login.current_user.login)