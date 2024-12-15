from app.repositories.address_repository import AddressRepository

class AddressService:
    @staticmethod
    def add_address(user_id, street, city, state, zip_code, country):
        return AddressRepository.create_address(user_id, street, city, state, zip_code, country) 