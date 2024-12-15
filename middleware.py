from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt, create_access_token as jwt_create_access_token
from functools import wraps
from app.models.user import User

def jwt_required_with_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
       
        verify_jwt_in_request()
        
       
        jwt_data = get_jwt()
        user_id = jwt_data['sub']  
        
        
        user = User.objects(id=user_id).first()
        if not user:
            return jsonify({
                "status": "error",
                "data": {},
                "message": "User not found"
            }), 404
        
       
        request.user = user
        return fn(*args, **kwargs)
    
    return wrapper

def create_access_token(identity, username, **kwargs):
    
    additional_claims = {
        'username': username  
    }
    return jwt_create_access_token(identity=identity, additional_claims=additional_claims, **kwargs)
