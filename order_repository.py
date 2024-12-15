from app.models.order import Order

class OrderRepository:
    @staticmethod
    def create_order(user_id, product_ids, order_id, status, address):
        order = Order(user_id=user_id, products=product_ids, order_id=order_id, status=status, address=address)
        order.save()
        return order

    @staticmethod
    def get_orders_by_user(user_id):
        return Order.objects(user_id=user_id)  # Return all orders for the user