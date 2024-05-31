import flask
import flask_login
import os
import pandas
from project.settings import DATABASE
from registration_page.models import User, Product
from .app import shop
from PIL import Image
def render_shop_page():
    mod = False
    type1 = None
    id = None
    if flask.request.method == "POST":
        try:
        
            if flask.request.form["send"].split(";")[1] == "IMG":
            
                print(flask.request.form["send"])
                print(os.path.abspath(__file__+"/../static/image"))
                
                img = flask.request.files.get('image')
                print(img, type(img))
                # image = Image.open(img)
                # print(image, type(image))
                # image.show()
            elif flask.request.form["send"].split(";")[1] == "TEXT":
                text = flask.request.form["text"]
                id = flask.request.form["send"].split(";")[0]
                for product in Product.query.all():
                    if product.id == id:
                        product.name = text
        except :
            try:
                print(flask.request.form['img'])
                id = flask.request.form['img']
                type1 = "IMG"
                
            except:
                pass
            mod = True
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
        read_excel = pandas.read_excel(io=path_excel,header=None,names=["name", "description","count","price","discount"])
        for row in read_excel.iterrows():
            row_excel = row[1]
            product  = Product(
                name= row_excel["name"],
                description =row_excel["description"],
                count = row_excel["count"],
                price = row_excel["price"],
                discount = row_excel["discount"]
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
    list_admins=["Illya","Mykola Skrypnik"]
    print()
    admin=flask_login.current_user.login in list_admins
    cookie = flask.make_response(
        flask.render_template(template_name_or_list="shop.html",
                              name=flask_login.current_user.login, 
                              products = Product.query.all(),
                              count = count,
                              int = int,
                              admin =admin,
                              type = type1,
                              mod = mod,
                              id = id
                              ))
    # cookie.set_cookie("all", count)
    
    return cookie