from flask import Blueprint, request, jsonify
from app.services.wishlist_service import WishlistService
from app.models.product import Product  # Ensure Product model is imported
from app.middleware import jwt_required_with_user  # Import the custom middleware

wishlist_bp = Blueprint('wishlist', __name__)

@wishlist_bp.route('/wishlist', methods=['POST'])
@jwt_required_with_user
def add_to_wishlist():
    current_user = request.user  # Access the user from the request context
    data = request.get_json()
    product_id = data['product_id']
    product = Product.objects(id=product_id).first()
    if product:
        WishlistService.add_to_wishlist(current_user.id, product)
        return jsonify({
            "status": "success",
            "data": {
                "message": "Product added to wishlist"
            },
            "message": None
        }), 201
    return jsonify({
        "status": "error",
        "data": {},
        "message": "Product not found"
    }), 404

@wishlist_bp.route('/wishlist', methods=['GET'])
@jwt_required_with_user
def get_wishlist():
    current_user = request.user  # Access the user from the request context
    wishlist_data = WishlistService.get_wishlist(current_user.id)
    return jsonify({
        "status": "success",
        "data": {
            "wishlist": wishlist_data  # Return serialized product data
        },
        "message": None
    }), 200

@wishlist_bp.route('/wishlist', methods=['DELETE'])
@jwt_required_with_user
def remove_from_wishlist():
    current_user = request.user  # Access the user from the request context
    data = request.get_json()
    product_id = data['product_id']
    product = Product.objects(id=product_id).first()
    if product:
        WishlistService.remove_from_wishlist(current_user.id, product)
        return jsonify({
            "status": "success",
            "data": {
                "message": "Product removed from wishlist"
            },
            "message": None
        }), 200
    return jsonify({
        "status": "error",
        "data": {},
        "message": "Product not found"
    }), 404 