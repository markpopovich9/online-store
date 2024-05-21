import flask
import flask_login
import os
import pandas
from project.settings import DATABASE
from registration_page.models import User, Product
from .app import shop
def render_shop_page():
    try:
        count =  len(flask.request.cookies.get('products').split(" "))
        if flask.request.cookies.get('products').split(" ")[0]== "":
            count = "0"
    except:
        count = "0"
    # if flask.request.method == "POST":
        # count = str(int(count) + 1)
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
    
    # print(cookie_get)
    print(User.query.count(),User.query.all(),type(User.query.all()))
    # for product in User.query.all():
    # if count == None:
    #     count = '0'
    cookie = flask.make_response(
        flask.render_template(template_name_or_list="shop.html",
                              name=flask_login.current_user.login, 
                              products = Product.query.all(),
                              count = count
                              ))
    # cookie.set_cookie("all", count)
    
    return cookie