import React from 'react';
import { Link } from 'react-router-dom';
import { Product } from '../../types/product';
import { PriceDisplay } from './PriceDisplay';
import { API_URL } from '../../constants';
interface ProductCardProps {
  product: Product;
}

export const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  return (
    <Link to={`/product/${product.id}`} className="group">
      <div className="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-lg bg-gray-200 xl:aspect-h-8 xl:aspect-w-7">
        <img
          src={`${product.product_urls[0]}`}
          alt={product.product_name}
          className="h-32 w-full object-cover object-center group-hover:opacity-75"
        />
      </div>
      <div className="mt-2 space-y-1">
        <h3 className="text-sm text-gray-700 font-medium line-clamp-2">{product.product_name}</h3>
        <p className="text-sm text-gray-500 line-clamp-1">{product.product_description}</p>
        <PriceDisplay price={product.price} specialPrice={product.special_price} />
        <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
          product.is_available ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
        }`}>
          {product.is_available ? 'In Stock' : 'Out of Stock'}
        </span>
      </div>
    </Link>
  );
};