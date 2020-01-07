from flask import Blueprint, request
from app.models.user import User

userBlueprint = Blueprint('user', __name__)


@userBlueprint.route('/signup', methods=['POST'])
def signup():
    facebook_id = request.json.get('facebook_id')
    email = request.json.get('email')
    name = request.json.get('name')
    pic = request.json.get('pic')
    facebook_token = request.json.get('facebook_token')

    user = User(
        facebook_id=facebook_id,
        email=email,
        name=name,
        pic=pic,
        facebook_token=facebook_token
    )

    user.create()

    return "ok"
