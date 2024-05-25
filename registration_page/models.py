from project.settings import DATABASE
import flask_login
class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    login= DATABASE.Column(DATABASE.String(55))
    email= DATABASE.Column(DATABASE.String(255))
    password =  DATABASE.Column(DATABASE.String(255))
    def __repr__(self) -> str:
        return f"login - {self.login}"
class Product(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(60))
    description = DATABASE.Column(DATABASE.Text)
    count = DATABASE.Column(DATABASE.Integer)
    price = DATABASE.Column(DATABASE.Integer)
    discount = DATABASE.Column(DATABASE.Integer)
    def __repr__(self) -> str:
        return f"id - {self.id}"