from app.models.product import Product

class ProductRepository:
    @staticmethod
    def create_product(product_name, price, special_price, product_description, category, is_available, product_urls):
        product = Product(
            product_name=product_name,
            price=price,
            special_price=special_price,
            product_description=product_description,
            category=category,
            is_available=is_available,
            product_urls=product_urls
        )
        product.save()
        return product

    @staticmethod
    def get_all_products(page=1, per_page=10):
        return Product.objects.skip((page - 1) * per_page).limit(per_page)

    @staticmethod
    def find_product_by_id(product_id):
        return Product.objects(id=product_id).first()

    @staticmethod
    def search_products(search_term):
        # Use case-insensitive regex for searching
        return Product.objects(product_name__icontains=search_term).limit(10)