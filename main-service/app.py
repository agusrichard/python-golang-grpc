from flask import Flask, jsonify
from auth.auth import auth_blueprint
from todo.todo import todo_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(todo_blueprint, url_prefix='/todo')

@app.route('/', methods=['GET'])
def root_route():
    return jsonify({
        'message': 'Welcome to the todo app'
    })

if __name__ == '__main__':
    app.run(debug=True)