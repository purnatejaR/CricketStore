import React from 'react';
import { Shield, Truck } from 'lucide-react';

export const ProductFeatures: React.FC = () => {
  return (
    <div className="mt-8 border-t border-gray-200 pt-8">
      <h3 className="text-lg font-medium text-gray-900">Features</h3>
      <div className="mt-4 grid grid-cols-1 gap-4">
        <div className="flex items-start">
          <Shield className="h-6 w-6 text-green-500 flex-shrink-0" />
          <div className="ml-3">
            <h4 className="text-sm font-medium text-gray-900">Secure Payment</h4>
            <p className="mt-1 text-sm text-gray-500">All transactions are secure and encrypted</p>
          </div>
        </div>
        <div className="flex items-start">
          <Truck className="h-6 w-6 text-blue-500 flex-shrink-0" />
          <div className="ml-3">
            <h4 className="text-sm font-medium text-gray-900">Fast Delivery</h4>
            <p className="mt-1 text-sm text-gray-500">Free delivery for orders above ₹999</p>
          </div>
        </div>
      </div>
    </div>
  );
};