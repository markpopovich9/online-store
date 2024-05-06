import flask
import flask_login
import os
import pandas
from project.settings import DATABASE
from registration_page.models import User, Product

def render_shop_page():
    if len(list(Product.query.all())) == 0:
        path_excel=os.path.abspath(__file__ + "/../static/xlsx/Product.xlsx")
        read_excel = pandas.read_excel(io=path_excel,header=None,names=["name", "description","count","price"])
        for row in read_excel.iterrows():
            row_excel = row[1]
            product  = Product(
                name= row_excel["name"],
                description =row_excel["description"],
                count = row_excel["count"],
                price = row_excel["price"] 
            )
            DATABASE.session.add(product)
        DATABASE.session.commit()
            
    # products = {
        
    # }
    print(User.query.count(),User.query.all(),type(User.query.all()))
    # for product in User.query.all():
        
    return flask.render_template(template_name_or_list="shop.html",name=flask_login.current_user.login, products = Product.query.all())