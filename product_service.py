from app.repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def create_product(product_name, price, special_price, product_description, category, is_available, product_urls):
        return ProductRepository.create_product(product_name, price, special_price, product_description, category, is_available, product_urls)

    @staticmethod
    def get_all_products(page=1, per_page=10):
        return ProductRepository.get_all_products(page, per_page)

    @staticmethod
    def find_product_by_id(product_id):
        return ProductRepository.find_product_by_id(product_id)