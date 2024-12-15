from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from app.routes.auth_routes import auth_bp
from app.routes.product_routes import product_bp
from app.routes.order_routes import order_bp
from app.routes.cart_routes import cart_bp  
from app.routes.wishlist_routes import wishlist_bp  
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='app/static')  

@app.after_request
def set_headers(response):
    response.headers["Referrer-Policy"] = 'no-referrer'
    return response

app.config['MONGODB_SETTINGS'] = {
    'host': os.getenv('MONGO_URI')
}
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

db = MongoEngine(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(order_bp, url_prefix='/api')
app.register_blueprint(cart_bp, url_prefix='/api')  
app.register_blueprint(wishlist_bp, url_prefix='/api')  
if __name__ == '__main__':
    app.run(debug=True) 