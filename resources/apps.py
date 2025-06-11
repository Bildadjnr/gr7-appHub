from flask_restful import Resource
from models import App


class AppResource(Resource):
    def get(self, id=None):
        if id == None:
            apps = App.query.all()
            return apps

        else:
            app = App.query.filter_by(id=id).first()
            return app

    def post(self):
        return {"message": "App created successfully"}

    def delete(self, id):
        return {"message": "app deleted successfully"}
