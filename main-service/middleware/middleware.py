import json
import functools
from flask import request, g, Response, jsonify
from auth.auth import AuthClient


def token_required(func):
    """To validate user with token authentication"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers.get('token')
            auth_client = AuthClient()
            result = auth_client.validate_token(token=token)
            g.user_data = json.loads(result.message)
            return func(*args, **kwargs)
        except:
            res = jsonify({'success': False, 'message': 'Invalid token'})
            return res

    return wrapper