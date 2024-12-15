from app.repositories.product_repository import ProductRepository

class SearchService:
    @staticmethod
    def search_products(search_term):
        return ProductRepository.search_products(search_term) 