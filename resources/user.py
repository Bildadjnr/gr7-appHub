from flask_restful import Resource
from models import User, db
from flask import request


class UserResource(Resource):
    def get(self, id=None):
        if id is None:
            users = User.query.all()
            return [user.to_dict() for user in users]
        else:
            user = User.query.filter_by(id=id).first()
            return user.to_dict()

    def post(self, id=None):
        data = request.get_json()

        new_user = User(
            name=data["name"],
            email=data["email"],
            # created_at=datetime(data["created_at"])
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict()

    def patch(self, id):
        data = request.get_json()
        User.query.filter_by(id=id).update(data)
        db.session.commit()
        return {"message": "User updated successfully"}
        

    def delete(self, id):
        deleted_user = User.query.filter_by(id= id).first()
        db.session.delete(deleted_user)
        db.session.commit()
        return {"message": "User deleted successfully"}
