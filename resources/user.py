from flask_restful import Resource
from models import User


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id == None:
            users = User.query.all()
            return users
        else:
            user = User.query.filter_by(user_id=user_id).first()
            return user

    def post(self):
        return {"message": "User created"}

    def patch(self, user_id):
        return {"message": "User updated"}

    def delete(self, user_id):
        return {"message": "User deleted"}
