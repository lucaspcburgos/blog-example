from flask import Blueprint, request
from app.models.user import User

userBlueprint = Blueprint('user', __name__)


@userBlueprint.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    name = request.json.get('name')
    pic = request.json.get('pic')

    user = User(
        email=email,
        name=name,
        pic=pic
    )

    user.create()

    return "ok"
