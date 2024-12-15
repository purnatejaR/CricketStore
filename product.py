from mongoengine import Document, StringField, FloatField, ListField, BooleanField
from app.models.schemas import ProductSchema

class Product(Document):
    product_name = StringField(required=True)
    price = FloatField(required=True)
    special_price = FloatField(default=0.0)
    product_description = StringField()
    category = StringField(required=True)
    is_available = BooleanField(default=True)
    product_urls = ListField(StringField())

    def serialize(self):
        product_schema = ProductSchema()
        return product_schema.dump(self)