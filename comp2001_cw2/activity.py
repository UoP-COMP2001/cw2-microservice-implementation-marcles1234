from flask import abort, make_response

from config import db
from models import Activity, activity_schema, Users

def read_one(Activity_ID):
    activity = Activity.query.get(Activity_ID)

    if activity is not None:
        return activity_schema.dump(activity)
    else:
        abort(
            404, f"Activity with ID {Activity_ID} not found"
        )


def update(Activity_ID, activity):
    existing_activity = Activity.query.get(Activity_ID)

    if existing_activity:
        update_activity = activity_schema.load(activity, session=db.session)
        existing_activity.content = update_activity.content
        db.session.merge(existing_activity)
        db.session.commit()
        return note_schema.dump(existing_activity), 201
    else:
        abort(404, f"Activity with ID {Activity_ID} not found")

def delete(Activity_ID):
    existing_activity = Activity.query.get(Activity_ID)

    if existing_activity:
        db.session.delete(existing_activity)
        db.session.commit()
        return make_response(f"{Activity_ID} successfully deleted", 204)
    else:
        abort(404, f"Activity with ID {Activity_ID} not found")


def create(activity):
    User_ID = activity.get("User_ID")
    user = Users.query.get(User_ID)

    if user:
        activity_data = {"Favourite_activity": activity.get("Favourite_activity")}
        new_activity = activity_schema.load(activity_data, session=db.session)
        db.session.add(new_activity)
        user.activity.append(new_activity)
        db.session.commit()
        return activity_schema.dump(new_activity), 201
    else:
        abort(
            404,
            f"User not found for ID: {User_ID}"
        )

