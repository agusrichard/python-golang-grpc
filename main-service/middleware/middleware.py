import json
import functools
from flask import request, Response, jsonify, session, redirect, url_for
from auth.auth import AuthClient


def token_required(func):
    """To validate user with token authentication"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token = session.get('token') or ''
            auth_client = AuthClient()
            result = auth_client.validate_token(token=token)
            session['user_data'] = json.loads(result.message)
            return func(*args, **kwargs)
        except Exception as error:
            print('error', error)
            return redirect(url_for('auth_blueprint.login'))

    return wrapper