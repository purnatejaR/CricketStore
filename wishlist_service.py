from app.repositories.wishlist_repository import WishlistRepository
from app.models.product import Product  
class WishlistService:
    @staticmethod
    def add_to_wishlist(user_id, product):
        return WishlistRepository.add_to_wishlist(user_id, product)

    @staticmethod
    def get_wishlist(user_id):
        wishlist = WishlistRepository.get_wishlist(user_id)
        # Serialize the products in the wishlist
        return [product.serialize() for product in wishlist.products] if wishlist else []

    @staticmethod
    def remove_from_wishlist(user_id, product):
        return WishlistRepository.remove_from_wishlist(user_id, product) 