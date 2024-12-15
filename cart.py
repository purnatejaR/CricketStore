from mongoengine import Document, ReferenceField, ListField
from app.models.schemas import CartSchema

class Cart(Document):
    user_id = ReferenceField('User', required=True)
    products = ListField(ReferenceField('Product'))  # List of products in the cart

    def serialize(self):
        cart_schema = CartSchema()
        return cart_schema.dump(self)