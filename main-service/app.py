from flask import Flask, jsonify, render_template
from auth.auth import auth_blueprint
from todo.todo import todo_blueprint

app = Flask(__name__)

app.secret_key = 'ThisIsExtremelySecretKey'

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(todo_blueprint, url_prefix='/todo')

@app.route('/', methods=['GET'])
def root_route():
    return render_template('home.html')