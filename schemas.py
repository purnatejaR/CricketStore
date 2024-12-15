from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))

class ProductSchema(Schema):
    id = fields.Str(dump_only=True)
    product_name = fields.Str(required=True)
    price = fields.Float(required=True)
    special_price = fields.Float(missing=0.0) 
    product_description = fields.Str()
    category = fields.Str(required=True)
    is_available = fields.Bool(missing=True)  
    product_urls = fields.List(fields.Str(), required=True)

class CartSchema(Schema):
    user_id = fields.Str(required=True)
    products = fields.List(fields.Str(), required=True)  

class AddressSchema(Schema):
    user_id = fields.Str(required=True)
    street = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    zip_code = fields.Str(required=True)
    country = fields.Str(required=True)
    
class OrderSchema(Schema):
    user_id = fields.Str(required=True)
    products = fields.List(fields.Str(), required=True)  
    order_id = fields.Str(required=True)
    status = fields.Str(required=True)  
    address = fields.Nested(AddressSchema)  

class WishlistSchema(Schema):
    user_id = fields.Str(required=True)
    products = fields.List(fields.Str(), required=True)  

