import flask

home =  flask.Blueprint(
    name="home",
    import_name="app",
    template_folder="home_page/templates",
    static_folder= "home_page/static",
    static_url_path=  '/home/'
    
)