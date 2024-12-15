from mongoengine import Document, StringField, ReferenceField
from app.models.user import User

class Address(Document):
    user_id = ReferenceField(User, required=True)
    street = StringField(required=True)
    city = StringField(required=True)
    state = StringField(required=True)
    zip_code = StringField(required=True)
    country = StringField(required=True)

    def serialize(self):
        return {
            "user_id": str(self.user_id.id),
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country
        } 