
from flask import Flask
from resources.user import UserResource
from flask_restful import Api

app = Flask(__name__)

# link flask-restful with flask
api = Api(app)


#routes 
@app.get("/")
def index():
    return {"message": "Welcome to Group 7 app"}


#user
# @app.post("/users")
# def create_user():
#     return {"message": "user created successfully"}

#to retrieve all users 
# @app.get("/users")
# def get_all_users():
#     return []

#to retrieve a single user 
# @app.get("/users/<id>")
# def get_single_user (id):
#     return {}

#to update a user
# @app.patch("/users/<id>")
# def update_user(id):
#     return {"message": "user updated successfully"}

#to delete a user 
# @app.delete("/users/<id>")
# def delete_user(id):
#     return {"message": "user deleted successfully"}

#APP
#creating app
@app.post("/apps")
def create_app():
    return {"message": "app created successfully"}


# to retrieve all apps
@app.get("/apps")
def get_all_apps():
    return []


# to retrieve a single app
@app.get("/apps/<id>")
def get_single_app(id):
    return {}


# to update app
@app.patch("/apps/<id>")
def update_app(id):
    return {"message": "app updated successfully"}


# to delete an app
@app.delete("/apps/<id>")
def delete_app(id):
    return {"message": "app deleted successfully"}

#DOWNLOAD

#creating download
@app.post("/downloads")
def create_download():
    return {"message": "download created successfully"}

# to retrieve all downloads
@app.get("/downloads")
def get_all_downloads():
    return []


# to retrieve a single download
@app.get("/downloads/<id>")
def get_single_download(id):
    return {}


# to delete download
@app.delete("/downloads/<id>")
def delete_download(id):
    return {"message": "download deleted successfully"}

#REVIEW

#creating a review
@app.post("/reviews")
def create_review():
    return {"message": "review created successfully"}


# to retrieve all reviews
@app.get("/reviews")
def get_all_reviews():
    return []


# to retrieve a single review
@app.get("/reviews/<id>")
def get_single_review(id):
    return {}


# to update a review
@app.patch("/reviews/<id>")
def update_review(id):
    return {"message": "review updated successfully"}


# to delete a review
@app.delete("/reviews/<id>")
def delete_review(id):
    return {"message": "review deleted successfully"}


api.add_resource(UserResource, "/users", "/users/<user_id>")
