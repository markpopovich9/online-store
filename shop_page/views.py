import flask
import flask_login
import os
import pandas
from project.settings import DATABASE
from registration_page.models import User, Product
from .app import shop
from PIL import Image
dict_types={
    "IMG":"IMG",
    "NAME":"TEXT",
    "PRICE":"INT"
}
def render_shop_page():
    mod = False
    type1 = None
    id = None
    if flask.request.method == "POST":
        try:
            flask.request.form["send"].split(";")[1]
            type1 = flask.request.form["send"].split(";")[1]

            if type1 == "IMG":
                id = int(flask.request.form["send"].split(";")[0])
                path= os.path.abspath(__file__ + "/../static/image/"+ Product.query.all()[id-1].name+ ".png") 
                

                print(flask.request.form["send"])

                # print(os.path.abspath(__file__+"/../static/image"))
                print(path)
                img = flask.request.files.get('image')
                print(img.filename, 11)
                if img.filename != "":
                    os.remove(path)
                    img.save(path)
                print(img, type(img))
                # image = Image.open(img)
                # print(image, type(image))
                # image.show()
                os.rename
            elif dict_types[type1] == "TEXT" or dict_types[type1] == "INT":
                next = True
                text = flask.request.form['text']
                if dict_types[type1] == "INT":
                    try:
                        int(text)
                    except:
                        next = False
                if text != "" and next:
                    id = flask.request.form["send"].split(";")[0]
                    list_products = Product.query.all()
                    for product in Product.query.all():
                        Product.query.filter_by(id = product.id).delete()
                    print(124)
                    for product_data in list_products:
                        name = product_data.name
                        count = product_data.count
                        price = product_data.price
                        discount = product_data.discount
                        print(name,price,discount, count)
                        if product_data.id == int(id):
                            if type1 == "NAME":

                                path1 = os.path.abspath(__file__ + "/../static/image/"+name+ ".png")
                                path2 = os.path.abspath(__file__ + "/../static/image/"+text+ ".png")
                                os.rename(path1,path2)
                                name = text
                            elif type1 == "PRICE":
                                price = flask.request.form['text']
                            # print(123)
                        # print(126)
                        product  = Product(
                            name= name ,
                            description =product_data.description,
                            count = count,
                            price = price,
                            discount = discount
                        )
                        DATABASE.session.add(product)
                    print(125)
                    DATABASE.session.commit()
            # elif dict_types[type1] == "INT":
            #     try:

            #     except:
        except Exception as Error:
            print(Error)
            try:
                print(flask.request.form['img'])
                id = flask.request.form['img']
                type1 = "IMG"
                
            except:
                try:
                    id = flask.request.form['name']
                    type1 = "NAME"
                except:
                    
                    try:
                        print(flask.request.form)
                        id = flask.request.form['price']
                        print('1')
                        type1 = "PRICE"
                        print('2')
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
    print(Product)
    if len(Product.query.all()) == 0:
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