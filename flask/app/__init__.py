from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    print(type(app))
    # Flask 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ubicomp407!@192.168.1.186/IMS'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  
    migrate = Migrate(app, db)

    # with app.app_context():
    #     db.create_all()
    
    from app.api.incident_api import create_update_status_blueprint
    from app.api.log_api import log_api
    
    update_status = create_update_status_blueprint()

    app.register_blueprint(update_status, url_prefix='/api')
    app.register_blueprint(log_api, url_prefix='/api')

    # 모델 임포트 (db.init_app(app) 후에 임포트)
    from app.models.incident import Incident
    from app.models.log import Log

    return app

