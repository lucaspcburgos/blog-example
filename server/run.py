from app import app
from flask import jsonify
from config import HOST, PORT
from config.database import create_database

create_database(app)


@app.route('/')
def home():
    return jsonify(
        success=True,
        status='running'
    ), 200


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
