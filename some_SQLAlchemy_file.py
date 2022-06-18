from flask_sqlalchemy import SQLAlchemy, db
import sys

from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# moment = Moment(app)
# db = db_setup(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Enable debug mode.
app.config['DEBUG'] = True

db = SQLAlchemy(app)
Migrate(app, db)


class Vehicle(db.Model):
    __table__ = 'vehicle'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    model=db.Column(db.String, nullable=False)
    driver_id=db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)


class Driver(db.Model):
    __table__ = 'driver'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

