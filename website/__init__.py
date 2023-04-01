from flask import Flask
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path



db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "TPYfvwikxqxYrtPNOXTTHyTO00E0Y05Y"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSON_AS_ASCII'] = False
    db.init_app(app)
    

    from .views import views
    from .api import api
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")

    
    
    with app.app_context():
        db.create_all()
        
            
    return app
 