from app import app
from flask import jsonify
from config import HOST, PORT
from config.database import create_database
from app.controllers.user import userBlueprint

create_database(app)

app.register_blueprint(userBlueprint, url_prefix='/user')


@app.route('/')
def home():
    return jsonify(
        success=True,
        status='running'
    ), 200


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
