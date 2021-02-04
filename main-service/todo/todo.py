import json
from flask import Blueprint, g, jsonify, request

from todo.client import TodoClient
from middleware.middleware import token_required

todo_blueprint = Blueprint('todo_blueprint', __name__)


@todo_blueprint.route('/create', methods=['POST'])
@token_required
def create_todo():
    try:
        user_data = g.user_data
        title = request.json.get('title')
        description = request.json.get('description')
        print(user_data, title, description)
        client = TodoClient()
        result = client.create_todo(title=title,
                                    description=description,
                                    user_id=user_data.get('ID'))
        return jsonify({'success': True, 'message': result.message})
    except:
        return jsonify({'success': False, 'message': result.message})


@todo_blueprint.route('/get', methods=['GET'])
@token_required
def get_todos():
    try:
        user_data = g.user_data
        client = TodoClient()
        result = client.get_todos(user_id=user_data.get('ID'))
        return jsonify({
            'success': True,
            'message': result.message,
            'data': json.loads(result.data)
        })
    except:
        return jsonify({
            'success': False,
            'message': result.message,
            'data': []
        })


@todo_blueprint.route('/update', methods=['PUT'])
@token_required
def update_todo():
    try:
        id = request.json.get('id')
        title = request.json.get('title')
        description = request.json.get('description')
        client = TodoClient()
        result = client.update_todo(title=title,
                                    description=description,
                                    id=id)
        return jsonify({'success': True, 'message': result.message})
    except:
        return jsonify({
            'success': False,
            'message': result.message,
            'data': []
        })


@todo_blueprint.route('/delete/<int:id>', methods=['DELETE'])
@token_required
def delete_todo(id):
    try:
        client = TodoClient()
        result = client.delete_todo(id)
        return jsonify({
            'success': False,
            'message': result.message,
        })
    except:
        return jsonify({
            'success': False,
            'message': result.message,
        })