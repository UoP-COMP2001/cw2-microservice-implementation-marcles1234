from datetime import datetime
from config import app, db
from models import Users, Activity, User_activity, Preference, User_preference


USERS = [
    {"User_ID": 1, "Name": "Grace Hopper", "Phone_Number": "1234567890", "Language": "English", "User_type": "Staff", "Password": "test"},
    {"User_ID": 2, "Name": "Tim Berners-Lee", "Phone_Number": "2345678901", "Language": "English", "User_type": "User", "Password": "password1"},
    {"User_ID": 3, "Name": "Ada Lovelace", "Phone_Number": "3456789012", "Language": "English", "User_type": "User", "Password": "abc!"},
]

ACTIVITIES = [
    {"Activity_ID": 1, "Favourite_activity": "Walking"},
    {"Activity_ID": 2, "Favourite_activity": "Running"},
    {"Activity_ID": 3, "Favourite_activity": "Jumping"},
]

USER_ACTIVITY = [
    {"User_ID": 1, "Activity_ID": 1},
    {"User_ID": 1, "Activity_ID": 2},
    {"User_ID": 2, "Activity_ID": 2},
    {"User_ID": 3, "Activity_ID": 3},
]


PREFERENCES = [
    {"Preference_ID": 1, "Preference": "Long trails"},
    {"Preference_ID": 2, "Preference": "Units: Metric"},
    {"Preference_ID": 3, "Preference": "Height: 120cm"},
]

USER_PREFERENCE = [
    {"User_ID": 1, "Preference_ID": 1},
    {"User_ID": 2, "Preference_ID": 2},
    {"User_ID": 3, "Preference_ID": 3},
]



with app.app_context():
    db.drop_all()
    db.create_all()


    for user in USERS:
        db.session.add(Users(
            User_ID=user["User_ID"],
            Name=user["Name"],
            Phone_Number=user["Phone_Number"],
            Language=user["Language"],
            User_type=user["User_type"],
            Password=user["Password"]
        ))
    db.session.commit()


    for act in ACTIVITIES:
        db.session.add(Activity(
           Activity_ID=act["Activity_ID"],
            Favourite_activity=act["Favourite_activity"]
        ))

 

    for ua in USER_ACTIVITY:
        db.session.add(User_activity(
            User_ID=ua["User_ID"],
            Activity_ID=ua["Activity_ID"]
        ))
    db.session.commit()


    for pref in PREFERENCES:
        db.session.add(Preference(
            Preference_ID=pref["Preference_ID"],
            Preference=pref["Preference"]
        ))


    for up in USER_PREFERENCE:
        db.session.add(User_preference(
            User_ID=up["User_ID"],
            Preference_ID=up["Preference_ID"]
        ))

    db.session.commit()
