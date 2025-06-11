from flask_restful import Resource


class ReviewResource(Resource):
    def get(self, id=None):
        if id == None:
            return []
        else:
            return {}

    def post(self):
        return {"message": "Review Created successfully"}

    def patch(self, id):
        return {"message": "Review updated successfully"}

    def delete(self, id):
        return {"message": "Review deleted successfully"}
