from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import app

db = SQLAlchemy(app.app)
migration = Migrate(app.app, db)


def db_setup(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)


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
