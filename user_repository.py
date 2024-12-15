from app.models.user import User

class UserRepository:
    @staticmethod
    def create_user(username, email, password):
        user = User(username=username, email=email, password=password)
        user.save()
        return user

    @staticmethod
    def find_user_by_username(username):
        return User.objects(username=username).first()