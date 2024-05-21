import flask
import flask_login
from registration_page.models import User, Product

def render_contacts_page():
    try:
        count =  len(flask.request.cookies.get('products').split(" ")) # python + flask get
        if flask.request.cookies.get('products').split(" ")[0]== "":
            count = "0"
    except:
        count = "0"
    products = {}
    print(User.query.all(),type(User.query.all()))
    
    return flask.render_template(template_name_or_list="contacts.html",name=flask_login.current_user.login,count=count)