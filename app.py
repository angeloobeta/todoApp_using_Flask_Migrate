
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "Hello Word"

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all()
# db = SQLAlchemy(app)
# migration = (app,db)


# class Todo(db.Model):
#     __table__ = 'todos'
    
#     id = db.Column(db.Integer, primary_key=True)
#     description =  db.Column(db.String, nullable=False)

#     def __repr__(self):
#         return f'<Todo {self.id} {self.description}>'


if __name__ == '__main__':
   app.run(host="0.0.0.0")