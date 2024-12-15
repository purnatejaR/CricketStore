from flask import Blueprint, request, jsonify
from app.services.cart_service import CartService
from app.models.product import Product  # Ensure Product model is imported
from app.middleware import jwt_required_with_user  # Import the custom middleware

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
@jwt_required_with_user
def add_to_cart():
    current_user = request.user  # Access the user from the request context
    data = request.get_json()
    product_id = data['product_id']
    product = Product.objects(id=product_id).first()
    if product:
        CartService.add_to_cart(current_user.id, product)
        return jsonify({
            "status": "success",
            "data": {
                "message": "Product added to cart"
            },
            "message": None
        }), 201
    return jsonify({
        "status": "error",
        "data": {},
        "message": "Product not found"
    }), 404

@cart_bp.route('/cart', methods=['GET'])
@jwt_required_with_user
def get_cart():
    current_user = request.user  # Access the user from the request context
    cart_data = CartService.get_cart(current_user.id)
    return jsonify({
        "status": "success",
        "data": {
            "cart": cart_data  # Return serialized product data
        },
        "message": None
    }), 200

@cart_bp.route('/cart', methods=['DELETE'])
@jwt_required_with_user
def remove_from_cart():
    current_user = request.user  # Access the user from the request context
    data = request.get_json()
    product_id = data['product_id']
    product = Product.objects(id=product_id).first()
    if product:
        CartService.remove_from_cart(current_user.id, product)
        return jsonify({
            "status": "success",
            "data": {
                "message": "Product removed from cart"
            },
            "message": None
        }), 200
    return jsonify({
        "status": "error",
        "data": {},
        "message": "Product not found"
    }), 404 