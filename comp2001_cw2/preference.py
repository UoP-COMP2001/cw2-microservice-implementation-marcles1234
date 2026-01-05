from flask import abort, make_response

from config import db
from models import Preference, preference_schema, Users

def read_one(Preference_ID):
    preference = Preference.query.get(Preference_ID)

    if preference is not None:
        return preference_schema.dump(preference)
    else:
        abort(
            404, f"Preference with ID {Preference_ID} not found"
        )


def update(Preference_ID, preference):
    existing_preference = Preference.query.get(Preference_ID)

    if existing_preference:
        update_preference = preference_schema.load(preference, session=db.session)
        existing_preference.content = update_preference.content
        db.session.merge(existing_preference)
        db.session.commit()
        return note_schema.dump(existing_preference), 201
    else:
        abort(404, f"Preference with ID {Preference_ID} not found")

def delete(Preference_ID):
    existing_preference = Preference.query.get(Preference_ID)

    if existing_preference:
        db.session.delete(existing_preference)
        db.session.commit()
        return make_response(f"{Preference_ID} successfully deleted", 204)
    else:
        abort(404, f"Preference with ID {Preference_ID} not found")


def create(preference):
    User_ID = preference.get("User_ID")
    user = Users.query.get(User_ID)

    if user:
        preference_data = {"Preference": preference.get("Preference")}
        new_preference = preference_schema.load(preference_data, session=db.session)
        db.session.add(new_preference)
        user.preference.append(new_preference)
        db.session.commit()
        return preference_schema.dump(new_preference), 201
    else:
        abort(
            404,
            f"User not found for ID: {User_ID}"
        )

