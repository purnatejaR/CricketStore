from mongoengine import Document, ReferenceField, ListField
from app.models.schemas import WishlistSchema

class Wishlist(Document):
    user_id = ReferenceField('User', required=True)
    products = ListField(ReferenceField('Product'))  # List of products in the wishlist

    def serialize(self):
        wishlist_schema = WishlistSchema()
        return wishlist_schema.dump(self)