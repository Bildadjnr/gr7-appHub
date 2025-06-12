from sqlalchemy import MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# initialize metadata
metadata = MetaData()

# creating a db instance
db = SQLAlchemy(metadata=metadata)


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP)


class App(db.Model, SerializerMixin):
    __tablename__ = "apps"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("users.id"))
    created_at = db.Column(db.TIMESTAMP)

class Download(db.Model, SerializerMixin):
    __tablename__ = "downloads"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("users.id"))
    app_id = db.Column(db.Integer, ForeignKey("apps.id"))
    created_at = db.Column(db.TIMESTAMP)

class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("users.id"))
    app_id = db.Column(db.Integer, ForeignKey("apps.id"))
    created_at = db.Column(db.TIMESTAMP)
