from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER, DATABASE_MODIFICATIONS

DB = SQLAlchemy()


def create_database(app):

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DATABASE_MODIFICATIONS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        DATABASE_USER,
        DATABASE_PASSWORD,
        DATABASE_HOST,
        DATABASE_PORT,
        DATABASE_NAME
    )
    DB.init_app(app)
    with app.app_context():
        from app.models.user import User
        DB.create_all()
