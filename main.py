import os
from dotenv import load_dotenv
from flask import Flask

from app.model.DataBaseConfig import db
from app.controller.authController import authBp

from flask import jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

load_dotenv()

def resumeBuilder():
    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', "Secret-Key-resume-builder-2025")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'JWT_SECRET_KEY_resume-builder-2025')

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    app.register_blueprint(authBp, url_prefix='/v1/auth')

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to Resume Platform",
        })

    return app

if __name__ == '__main__':
    app = resumeBuilder()
    app.run(debug=True, host='0.0.0.0', port=3110)