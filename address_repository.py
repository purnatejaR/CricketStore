from app.models.address import Address

class AddressRepository:
    @staticmethod
    def create_address(user_id, street, city, state, zip_code, country):
        address = Address(user_id=user_id, street=street, city=city, state=state, zip_code=zip_code, country=country)
        address.save()
        return address

    @staticmethod
    def get_address_by_user(user_id):
        return Address.objects(user_id=user_id).first() 