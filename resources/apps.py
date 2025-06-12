from flask_restful import Resource
from models import App


class AppResource(Resource):
    def get(self, id=None):
        if id is None:
            apps = App.query.all()
            return [app.to_dict() for app in apps]
        else:
            app = App.query.filter_by(id=id).first()
            return app.to_dict()

    def post(self):
        return {"message": "App created successfully"}

    def delete(self, id):
        return {"message": "app deleted successfully"}
