import random
import string
from app.repositories.order_repository import OrderRepository
from app.repositories.address_repository import AddressRepository

class OrderService:
    @staticmethod
    def create_order(user_id, product_ids, address_data):
        order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        status = "pending" 
        
        
        address = AddressRepository.create_address(
            user_id=user_id,
            street=address_data['street'],
            city=address_data['city'],
            state=address_data['state'],
            zip_code=address_data['zip_code'],
            country=address_data['country']
        )
        
        
        order = OrderRepository.create_order(user_id, product_ids, order_id, status, address)
        return order

    @staticmethod
    def get_orders_by_user(user_id):
        orders = OrderRepository.get_orders_by_user(user_id) 
        res_data = []
        for order in orders:
            _order = order.serialize()
            _order['products'] = [product.serialize() for product in order.products] if order else []
            _order['address'] = order.address.serialize() if order.address else None  
            res_data.append(_order)
        return res_data  