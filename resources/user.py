from flask_restful import Resource

class UserResource(Resource):

    def get(self, user_id = None):
        if user_id == None:
            return []
        else :
            return {}
        
    def post(self):
        return {"message": "User created"}

    def patch(self, user_id):
        return {"message": "User updated"}

    def delete(self, user_id):
        return {"message": "User deleted"}