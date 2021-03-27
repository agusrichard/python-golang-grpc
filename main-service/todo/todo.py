from flask import Blueprint, request, jsonify

todo_blueprint = Blueprint('todo', __name__)

@todo_blueprint.route('/', methods=['GET'])
def get_todos():
    return jsonify({
        'message': 'get todos route'
    })