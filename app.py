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


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=True)

    def __int__(self, id, name, description, completed):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f' {self.id} {self.name}'


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __int__(self, id, description, completed):
        self.id = id
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


db.create_all()


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

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = None
    try:
        # name = request.form.get('name', '')
        name = request.get_json()['name']
        # description = request.form.get('description', '')
        description = request.get_json()['description']
        person = Person(description=description, name=name)
        db.session.add(person)
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify({
            'description': person.description,
            'name': person.name,
            'id': person.id
        })
    # return render_template('create.html', data=Person.query.all())
    # return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', data=Person.query.all())


# db.create_all()


# @app.route('/')
# def index():
#     db = Todo.query.first()
#     return db.name


# db = SQLAlchemy(app)


if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    app.run()
