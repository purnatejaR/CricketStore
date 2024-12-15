from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response = AuthService.register(data['username'], data['email'], data['password'])
    try:
        if isinstance(response, dict):  # Check if it's an error message
            return jsonify({
                "status": "error",
                "data": {},
                "message": response['message']
            }), 400
        return jsonify({
            "status": "success",
            "data": response.serialize(),
            "message": None
        }), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "data": {},
            "message": str(e)
        }), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response = AuthService.login(data['username'], data['password'])
    if 'access_token' in response[0]:
        return jsonify({
            "status": "success",
            "data": {
                "access_token": response[0]['access_token']
            },
            "message": None
        }), 200
    return jsonify({
        "status": "error",
        "data": {},
        "message": response['message']
    }), 401