from app.repositories.cart_repository import CartRepository
from app.models.product import Product

class CartService:
    @staticmethod
    def add_to_cart(user_id, product):
        return CartRepository.add_to_cart(user_id, product)

    @staticmethod
    def get_cart(user_id):
        cart = CartRepository.get_cart(user_id)
        return [product.serialize() for product in cart.products] if cart else []

    @staticmethod
    def remove_from_cart(user_id, product):
        return CartRepository.remove_from_cart(user_id, product) 