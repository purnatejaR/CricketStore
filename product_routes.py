from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.middleware import jwt_required_with_user

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
@jwt_required_with_user
def create_product():
    data = request.get_json()
    product = ProductService.create_product(
        product_name=data['product_name'],
        price=data['price'],
        special_price=data.get('special_price', 0.0),  # Default to 0 if not provided
        product_description=data.get('product_description', ''),
        category=data['category'],
        is_available=data.get('is_available', True),  # Default to True if not provided
        product_urls=data['product_urls']
    )
    return jsonify({
        "status": "success",
        "data": product.serialize(),  # Assuming you have a serialize method
        "message": None
    }), 201

@product_bp.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)  # Default to page 1
    per_page = request.args.get('per_page', 10, type=int)  # Default to 10 products per page
    products = ProductService.get_all_products(page, per_page)
    return jsonify({
        "status": "success",
        "data": {
            "products": [product.serialize() for product in products]
        },
        "message": None
    }), 200

@product_bp.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.find_product_by_id(product_id)
    if product:
        return jsonify({
            "status": "success",
            "data": product.serialize(),
            "message": None
        }), 200
    return jsonify({
        "status": "error",
        "data": {},
        "message": "Product not found"
    }), 404