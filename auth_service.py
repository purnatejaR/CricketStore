from app.repositories.user_repository import UserRepository
from mongoengine import ValidationError
from app.middleware import create_access_token  

class AuthService:
    @staticmethod
    def register(username, email, password):
        try:
            user = UserRepository.create_user(username, email, password)
            return user  
        except ValidationError as e:
            return {'message': str(e)}, 400  
    @staticmethod
    def login(username, password):
        user = UserRepository.find_user_by_username(username)
        if user and user.password == password:  
            access_token = create_access_token(identity=str(user.id), username=user.username,expires_delta=False)  # Pass both user ID and username
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401