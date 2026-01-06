from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, ma
import pytz


#TABLES

class User_activity(db.Model):
    __tablename__ = "user_activity"
    __table_args__ = {"schema": "CW2"}
    User_ID = db.Column(db.Integer, db.ForeignKey("CW2.users.User_ID"), primary_key=True)
    Activity_ID = db.Column(db.Integer, db.ForeignKey("CW2.activity.Activity_ID"), primary_key=True)


class User_preference(db.Model):
    __tablename__ = "user_preference"
    __table_args__ = {"schema": "CW2"}
    User_ID = db.Column(db.Integer, db.ForeignKey("CW2.users.User_ID"), primary_key=True)
    Preference_ID = db.Column(db.Integer, db.ForeignKey("CW2.preference.Preference_ID"), primary_key=True)


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "CW2"}
    User_ID = db.Column("User_ID", db.Integer, primary_key=True)
    Name = db.Column("Name", db.String(32))
    Phone_Number = db.Column("Phone_Number", db.String(12))
    Language = db.Column("Language", db.String(32))
    User_type = db.Column("User_type", db.String(32))
    Password = db.Column("Password", db.String(32))


class Activity(db.Model):
    __tablename__ = "activity"
    __table_args__ = {"schema": "CW2"}
    Activity_ID = db.Column(db.Integer, primary_key=True)
    Favourite_activity = db.Column(db.String(64))


class Preference(db.Model):
    __tablename__ = "preference"
    __table_args__ = {"schema": "CW2"}
    Preference_ID = db.Column(db.Integer, primary_key=True)
    Preference = db.Column(db.String(64))


#TABLE RELATIONSHIPS

Users.activity = db.relationship(
        "Activity",
        secondary="CW2.user_activity",
        back_populates="users"
    )

Activity.users = db.relationship(
        "Users",
        secondary="CW2.user_activity",
        back_populates="activity"
    )


Users.preference = db.relationship(
        "Preference",
        secondary="CW2.user_preference",
        back_populates="users"
    )

Preference.users = db.relationship(
        "Users",
        secondary="CW2.user_preference",
        back_populates="preference"
    )


#SCHEMAS

class ActivitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Activity
        load_instance = True
        sqla_session = db.session


class PreferenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Preference
        load_instance = True
        sqla_session = db.session


class UserSchema(ma.SQLAlchemyAutoSchema):
    activity = ma.Nested(ActivitySchema, many=True)
    preference = ma.Nested(PreferenceSchema, many=True)
    class Meta:
        model = Users
        load_instance = True
        sqla_session = db.session
        include_relationships = True


activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)

preference_schema = PreferenceSchema()
preferences_schema = PreferenceSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

