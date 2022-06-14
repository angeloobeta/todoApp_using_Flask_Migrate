import sys
from os import abort

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)
migration = Migrate(app, db)


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f' {self.id} {self.name}'


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


# @app.route('/todos/create', methods=['POST'])
# def create_todo():
#     body = {}
#     error = False
#     try:
#         description = request.get_json()['description']
#         todo = Todo(description=description)
#         body['description'] = todo.description
#         db.session.add(todo)
#         db.session.commit()
#     except:
#         error = True
#         db.session.rollback()
#         print(sys.exc_info())
#     finally:
#         db.session.close()
#         if error == True:
#             abort(400)
#         else:
#             return jsonify(body)

@app.route('/')
def index():
    users = ['Ifeanyichukwu Obeta', 'Software Engineer']
    return render_template('index.html', datium=[
        {'description': "Todo Item 1"},
        {'description': "Todo Item 2"},
        {"description": "Todo Item 3"},
        {"description": "Todo Item 4"},
    ], user=users)


# @app.route('/')
# def index():
#     return render_template('edit_index.html', data=Todo.query.all())


# db.create_all()


# @app.route('/')
# def index():
#     db = Todo.query.first()
#     return db.name


# db = SQLAlchemy(app)


if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    app.run()
