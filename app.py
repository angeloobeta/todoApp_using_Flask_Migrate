from flask import Flask, render_template, request, redirect, url_for
from flask_moment import Moment
import config
from model import Person, db_setup

app = Flask(__name__)
moment = Moment(app)
db = db_setup(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Enable debug mode.
app.config['DEBUG'] = True


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
    return render_template('index.html', data=Person.query.all())


# @app.route('/todo/create', methods=['POST'])
# def create_todo():
#     name = request.form.get('name', '')
#     description = request.form.get('description', '')
#     person = Person(description=description, name=name)
#     db.session.add(person)
#     db.session.commit()
#     return redirect(url_for('edit.html', data=Person.query.all()))


# db.create_all()


# @app.route('/')
# def index():
#     db = Todo.query.first()
#     return db.name


# db = SQLAlchemy(app)


if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    app.run()
