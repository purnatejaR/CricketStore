from flask import Blueprint, request, jsonify
from app.services.address_service import AddressService
from app.middleware import jwt_required_with_user

address_bp = Blueprint('address', __name__)

@address_bp.route('/address', methods=['POST'])
@jwt_required_with_user
def add_address():
    current_user = request.user
    data = request.get_json()
    address = AddressService.add_address(
        user_id=current_user.id,
        street=data['street'],
        city=data['city'],
        state=data['state'],
        zip_code=data['zip_code'],
        country=data['country']
    )
    return jsonify({
        "status": "success",
        "data": address.serialize(),
        "message": None
    }), 201 