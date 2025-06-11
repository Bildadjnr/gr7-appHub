from flask_restful import Resource


class DownloadResource(Resource):
    def get(self, id=None):
        if id == None:
            return []
        else:
            return {}

    def post(self):
        return {"message": "downloaded successfully"}

    def delete(self, id):
        return {"message": "deleted successfully"}
