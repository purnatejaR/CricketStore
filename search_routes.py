from flask import Blueprint, request, jsonify
from app.services.search_service import SearchService

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('q', '', type=str)  # Get the search term from query parameters
    products = SearchService.search_products(search_term)
    return jsonify({
        "status": "success",
        "data": {
            "products": [product.serialize() for product in products]  # Serialize each product
        },
        "message": None
    }), 200 