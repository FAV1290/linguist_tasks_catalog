import uuid
import flask
import flask_login
from flask_wtf import CSRFProtect


from db.models import User
from webapp.blueprints import test_blueprint


def build_app() -> flask.Flask:
    app = flask.Flask(__name__)

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = '.user_sign_in'

    csrf = CSRFProtect()
    csrf.init_app(app)

    app.config.from_pyfile('config.py')
    app.register_blueprint(test_blueprint, url_prefix='/')

    @login_manager.user_loader
    def load_user(user_id: uuid.UUID) -> User | None:
        return User.query.get(user_id)
    return app
