from app.models.user import User
from app.models.wishlist import Wishlist

class WishlistRepository:
    @staticmethod
    def add_to_wishlist(user_id, product):
        user = User.objects(id=user_id).first()
        if user:
            # Check if the wishlist already exists
            wishlist = Wishlist.objects(user_id=user).first()
            if not wishlist:
                # Create a new wishlist if it doesn't exist
                wishlist = Wishlist(user_id=user)
                wishlist.save()
            # Add the product to the wishlist
            wishlist.products.append(product)
            wishlist.save()
            return wishlist
        return None

    @staticmethod
    def get_wishlist(user_id):
        return Wishlist.objects(user_id=user_id).first()

    @staticmethod
    def remove_from_wishlist(user_id, product):
        wishlist = Wishlist.objects(user_id=user_id).first()
        if wishlist and product in wishlist.products:
            wishlist.products.remove(product)
            wishlist.save()
            return wishlist
        return None 