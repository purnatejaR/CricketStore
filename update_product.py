import pandas as pd
from mongoengine import connect
import sys;sys.path.append('./')
from app.models.product import Product  
from dotenv import load_dotenv
import os

load_dotenv()
connect('sports_ecommerce', host=os.getenv('MONGO_URI'))  


def update_products_from_csv(csv_file):
    
    df = pd.read_csv(csv_file)  

    for index, row in df.iterrows():
        
        product_name = row['Product Name']
        price = row['Old Price']
        special_price = row['Special Price']
        product_description = row['Product Name']
        category = 'Sports'
        is_available = True
        
        product_urls = [row["Images"]]  
        
        product = Product.objects(product_name=product_name).first()

        if product:
            
            product.price = price
            product.special_price = special_price
            product.product_description = product_description
            product.category = category
            product.is_available = is_available
            product.product_urls = product_urls
            product.save()
            print(f"Updated product: {product_name}")
        else:
            
            new_product = Product(
                product_name=product_name,
                price=price,
                special_price=special_price,
                product_description=product_description,
                category=category,
                is_available=is_available,
                product_urls=product_urls
            )
            new_product.save()
            print(f"Created new product: {product_name}")

if __name__ == "__main__":
    update_products_from_csv('/Users/jaya.patibandla/Downloads/Sports_Ecommerce_Product_Data_updated.csv')
