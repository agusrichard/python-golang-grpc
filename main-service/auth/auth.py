from flask import Blueprint, request, jsonify

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['GET'])
def register():
    return jsonify({
        'message': 'register route'
    })

@auth_blueprint.route('/login', methods=['GET'])
def login():
    return jsonify({
        'message': 'Login route'
    })