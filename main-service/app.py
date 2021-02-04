from flask import Flask
from auth.auth import auth_blueprint
from todo.todo import todo_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(todo_blueprint, url_prefix='/todo')

if __name__ == '__main__':
    app.run(debug=True)