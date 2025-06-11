from flask import Flask
from resources.user import UserResource
from resources.apps import AppResource
from resources.download import DownloadResource
from resources.review import ReviewResource
from flask_restful import Api

app = Flask(__name__)

# link flask-restful with flask
api = Api(app)


# routes
@app.get("/")
def index():
    return {"message": "Welcome to Group 7 app"}


api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(AppResource, "/apps", "/apps/<int:id>")
api.add_resource(DownloadResource, "/downloads", "/downloads/<int:id>")
api.add_resource(ReviewResource, "/reviews", "/reviews/<int:id>")
