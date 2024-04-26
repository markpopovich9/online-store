import home_page
import registration_page
import login_page
from .settings import shop
home_page.home.add_url_rule(rule="/",view_func= home_page.render_home_page )
login_page.login.add_url_rule(rule= "/login/",view_func=login_page.render_login_page)
registration_page.reg.add_url_rule(rule="/reg/",view_func=registration_page.render_reg_page )
shop.register_blueprint(blueprint= home_page.home)
shop.register_blueprint(blueprint=registration_page.reg)

shop.register_blueprint(blueprint= login_page.login)