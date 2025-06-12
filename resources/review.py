from flask_restful import Resource
from models import Review


class ReviewResource(Resource):
    def get(self, id=None):
        if id is None:
            reviews = Review.query.all()
            return reviews
        else:
            review = Review.query.filter_by(id=id).first()
            return review

    def post(self):
        return {"message": "Review Created successfully"}

    def patch(self, id):
        return {"message": "Review updated successfully"}

    def delete(self, id):
        return {"message": "Review deleted successfully"}
