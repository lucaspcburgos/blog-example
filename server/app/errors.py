from flask import jsonify
from http import HTTPStatus


class DefaultErrors:
    @staticmethod
    def user_input_error(description):
        return jsonify(
            description=description
        ), HTTPStatus.FORBIDDEN
