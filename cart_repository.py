from app.models.user import User
from app.models.cart import Cart

class CartRepository:
    @staticmethod
    def add_to_cart(user_id, product):
        user = User.objects(id=user_id).first()
        if user:
            cart = Cart.objects(user_id=user).first()
            if not cart:
                cart = Cart(user_id=user)
                cart.save()
            cart.products.append(product)
            cart.save()
            return cart
        return None

    @staticmethod
    def get_cart(user_id):
        return Cart.objects(user_id=user_id).first()

    @staticmethod
    def remove_from_cart(user_id, product):
        cart = Cart.objects(user_id=user_id).first()
        if cart and product in cart.products:
            cart.products.remove(product)
            cart.save()
            return cart
        return None 