from mongoengine import Document, StringField, EmailField, ValidationError, ListField, ReferenceField
import re
from app.models.schemas import UserSchema

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    cart = ListField(ReferenceField('Product'))
    wishlist = ListField(ReferenceField('Product'))

    def clean(self):
        # Validate username
        if len(self.username) < 3:
            raise ValidationError("Username must be at least 3 characters long.")
        
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidationError("Invalid email format.")
        
        # Validate password strength
        if len(self.password) < 6:
            raise ValidationError("Password must be at least 6 characters long.")
        if not re.search(r"[A-Za-z]", self.password) or not re.search(r"[0-9]", self.password):
            raise ValidationError("Password must contain both letters and numbers.")

    def serialize(self):
        user_schema = UserSchema()
        return user_schema.dump(self)