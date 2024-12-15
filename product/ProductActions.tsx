import React from 'react';
import { ShoppingCart } from 'lucide-react';
import { addToCart } from '../../services/api';
import toast from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';

interface ProductActionsProps {
  isAvailable: boolean;
  productId: string;
}

export const ProductActions: React.FC<ProductActionsProps> = ({ isAvailable, productId }) => {
  const navigate = useNavigate();

  const handleAddToCart = async () => {
    if (isAvailable) {
      try {
        await addToCart(productId);
        toast.success('Product added to cart!');
      } catch (error) {
        toast.error('Failed to add product to cart.');
      }
    }
  };

  const handleBuyNow = () => {
    localStorage.setItem('productIds', JSON.stringify([productId])); // Store product ID in local storage
    navigate('/placeorder'); // Redirect to PlaceOrder page
  };

  return (
    <div className="mt-8">
      <button
        onClick={handleAddToCart}
        disabled={!isAvailable}
        className={`flex items-center justify-center w-full px-6 py-3 text-base font-medium rounded-md shadow-sm ${
          isAvailable
            ? 'bg-indigo-600 text-white hover:bg-indigo-700'
            : 'bg-gray-300 text-gray-500 cursor-not-allowed'
        }`}
      >
        <ShoppingCart className="w-5 h-5 mr-2" />
        {isAvailable ? 'Add to Cart' : 'Out of Stock'}
      </button>
      
      {isAvailable && (
        <button
          onClick={handleBuyNow}
          className="mt-4 flex items-center justify-center w-full px-6 py-3 text-base font-medium text-indigo-600 bg-indigo-100 border border-transparent rounded-md hover:bg-indigo-200"
        >
          Buy Now
        </button>
      )}
    </div>
  );
};