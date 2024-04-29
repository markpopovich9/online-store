import flask_login
from .settings import shop
from registration_page.models import User

shop.secret_key = "KEY"
login_manager = flask_login.LoginManager(app = shop)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)