from flask import abort, make_response
from config import db
from models import Users, users_schema


def read_all():
    users = Users.query.all()
    return users_schema.dump(users)


def create(user):
    Name = user.get("Name")
    Phone_number = user.get("Phone_number")
    Language_ID = user.get("Language_ID")

    if not Name:
        abort(400, "Name is required")

    new_user = user_schema.load(user, session=db.session)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.dump(new_user), 201


def read_one(User_ID):
    user = Users.query.filter(Users.User_ID == User_ID).one_or_none()
    if User_ID is not None:
        return user_schema.dump(user)
    else:
        abort(404, f"User with ID {User_ID} not found")


def update(User_ID, user):
    existing_user = Users.query.filter(Users.User_ID == User_ID).one_or_none()
    if existing_user:
        update_user = user_schema.load(user, session=db.session)
        existing_user.Name = update_user.Name
        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 201

    else:
        abort(404, f"User with ID {User_ID} not found")


def delete(User_ID):
    existing_user = Users.query.filter(Users.User_ID == User_ID).one_or_none()
    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(
            f"{User_ID} successfully deleted", 200)
    else:
        abort(
            404,
                f"Person with last name {User_ID} not found")

