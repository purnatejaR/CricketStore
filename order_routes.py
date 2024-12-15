from flask import Blueprint, request, jsonify
from app.middleware import jwt_required_with_user  # Import the custom middleware
from app.services.order_service import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/order', methods=['POST'])
@jwt_required_with_user
def create_order():
    current_user = request.user
    data = request.get_json()
    product_ids = data['product_ids']
    address_data = data['address']  # Expecting address data in the request
    order = OrderService.create_order(current_user.id, product_ids, address_data)
    return jsonify({
        "status": "success",
        "data": {
            "order_id": order.order_id,
            "address": order.address.serialize()  # Include address in the response
        },
        "message": None
    }), 201

@order_bp.route('/orders', methods=['GET'])
@jwt_required_with_user
def get_orders():
    current_user = request.user  # Access the user from the request context
    orders = OrderService.get_orders_by_user(current_user.id)
    return jsonify({
        "status": "success",
        "data": {
            "orders": orders  # Return serialized order data
        },
        "message": None
    }), 200