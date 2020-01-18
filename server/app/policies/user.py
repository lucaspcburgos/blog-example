from flask import request
from functools import wraps
from app.errors import DefaultErrors
from app.models.user import User


def validate_user_register(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        email = request.json.get('email')
        username = request.json.get('username')
        password = request.json.get('password')

        if not email:
            return DefaultErrors.user_input_error('E-mail is required')
        if not username:
            return DefaultErrors.user_input_error('Username is required')
        if not password:
            return DefaultErrors.user_input_error('Password is required')

        if User.query.filter_by(email=email).first():
            return DefaultErrors.user_input_error('This e-mail is already registered')
        elif User.query.filter_by(username=username).first():
            return DefaultErrors.user_input_error('This username is already registered')
        return f(*args, **kwargs)
    return decorated_function
