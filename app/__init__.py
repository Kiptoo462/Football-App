from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

mail = Mail()

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config_options[config_name])

    mail.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    
    login_manager.init_app(app)
    
    # Register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    #@login_manager.user_loader
    #def load_user(user_id):
        #user = User.query.filter_by(id=user_id).first()

    return app