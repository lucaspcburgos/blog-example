from flask import Blueprint, request, jsonify
from app.models.user import User
from app.policies.user import validate_user_register
# from app.errors import DefaultErrors

userBlueprint = Blueprint('user', __name__)


@userBlueprint.route('/signup', methods=['POST'])
@validate_user_register
def signup():
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')

    user = User(
        email=email,
        username=username,
        password=password
    )

    user.create()

    return jsonify(
        description='User created successfully'
    ), 201
