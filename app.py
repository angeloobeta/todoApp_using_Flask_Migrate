from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SQLAlchemy
from flask_migration import Migration
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

migration = Migration(app,db)


class Todo(db.Model):
    __table__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    description =  db.Column(db.String, nullable=False)
