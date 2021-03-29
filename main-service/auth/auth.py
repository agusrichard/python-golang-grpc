from flask import Blueprint, request, jsonify

from auth.client import AuthClient

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/register', methods=['POST'])
def register():
    auth_client = AuthClient()
    result = auth_client.register(username=request.json['username'],
                                  password=request.json['password'])
    return jsonify({'success': result.success, 'message': result.message})


@auth_blueprint.route('/login', methods=['POST'])
def login():
    auth_client = AuthClient()
    result = auth_client.login(username=request.json['username'],
                               password=request.json['password'])
    return jsonify({
        'success': result.success,
        'message': result.message,
        'token': result.token
    })
