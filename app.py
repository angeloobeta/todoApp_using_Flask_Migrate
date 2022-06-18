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


# def db_setup(app):
#     app.config.from_object('config')
#     db.app = app
#     db.init_app(app)
#     migration = Migrate(app, db)
#     return db


# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), nullable=False)
#     description = db.Column(db.String(), nullable=False)
#     completed = db.Column(db.Boolean, nullable=True)
#
#     def __int__(self, id, name, description, completed):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.completed = completed
#
#     def __repr__(self):
#         return f' {self.id} {self.name}'


class Todolist(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    todos = db.relationship('Todo', backref='list', lazy=True)


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolist.id'), nullable=False)

    def __int__(self, id, description, completed):
        self.id = id
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


@app.route('/todo/delete-item', methods=['DELETE'])
def delete_item():
    try:
        todo_id = request.get_json()['person_id']
        todo = Todo.query.get(todo_id)
        print(todo)
        db.session.delete(todo)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
        return redirect(url_for('create'))


@app.route('/todo/<todo_id>/set-completed', methods=['POST'])
def set_completed(todo_id):
    try:
        completed = request.get_json()['completed']
        print('complete', completed)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
        return redirect(url_for('create'))


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = None
    body = {}
    try:
        # name = request.form.get('name', '')
        name = request.get_json()['name']
        # description = request.form.get('description', '')
        description = request.get_json()['description']
        todo = Todo(description=description, name=name)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['name'] = todo.name
        body['description'] = todo.description
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)
    # return render_template('create.html', data=Person.query.all())
    # return redirect(url_for('index'))


@app.route('/')
def create():
    return render_template('create.html', data=Todo.query.order_by('id').all())


if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    app.run()
