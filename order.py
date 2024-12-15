from mongoengine import Document, ReferenceField, StringField, ListField
from app.models.schemas import OrderSchema
from app.models.address import Address  # Import the Address model

class Order(Document):
    user_id = ReferenceField('User', required=True)
    products = ListField(ReferenceField('Product'), required=True)
    order_id = StringField(required=True, unique=True)
    status = StringField(required=True)  # e.g., "pending", "completed", etc.
    address = ReferenceField(Address, required=True)  # Link to Address model

    def serialize(self):
        order_schema = OrderSchema()
        return order_schema.dump(self)