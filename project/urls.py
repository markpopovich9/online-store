from registration_page import reg,render_reg_page
from home_page import home,render_home_page
from login_page import login,render_login_page
from .settings import shop
home.add_url_rule(rule="/",view_func= render_home_page, methods = ['GET', 'POST'])
login.add_url_rule(rule= "/login/",view_func=render_login_page, methods=["GET","POST"])
reg.add_url_rule(rule="/reg/",view_func=render_reg_page, methods=["GET","POST"] )

shop.register_blueprint(blueprint= home)
shop.register_blueprint(blueprint=reg)

shop.register_blueprint(blueprint= login)