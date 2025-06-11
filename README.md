# AppHub API

This is a Flask-based RESTful API for managing an app marketplace called *AppHub*.

##  Features

- RESTful endpoints will manage:
  - *Users*
  - *Apps*
- Technologies used:
  - Flask
  - Flask-RESTful
  - SQLAlchemy (ORM)
  - Flask-Migrate with Alembic (for database migrations)
  - SQLite as the default database

##  Endpoints

### Users
- GET /users — List all users
- GET /users/<user_id> — Retrieve a single user
- POST /users — Create a user
- PATCH /users/<user_id> — Update a user
- DELETE /users/<user_id> — Delete a user

### Apps
- GET /apps — List all apps
- GET /apps/<id> — Retrieve a single app
- POST /apps — Create an app

## Database Models

- *User*
  - id: Integer, Primary Key
  - name: Text
  - email: Text
  - created_at: Timestamp

- *App*
  - id: Integer, Primary Key
  - name: Text
  - user_id: Foreign Key to User
  - created_at: Timestamp

##  Migrations

This project uses Alembic (via Flask-Migrate) to handle  migrations. The initial migration creates users and apps tables.

##Collaborators:
-Bildad Ereggae
-Maureen Nkirote
-Carol Kosgei
-Jeff Mbithi
-Brian Bett


