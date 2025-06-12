from flask_restful import Resource
from models import Download


class DownloadResource(Resource):
    def get(self, id=None):
        if id is None:
            downloads = Download.query.all()
            return downloads
        else:
            download = Download.query.filter_by(id=id).first()
            return download

    def post(self):
        return {"message": "downloaded successfully"}

    def delete(self, id):
        return {"message": "deleted successfully"}
