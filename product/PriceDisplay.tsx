import React from 'react';

interface PriceDisplayProps {
  price: number;
  specialPrice?: number;
}

export const PriceDisplay: React.FC<PriceDisplayProps> = ({ price, specialPrice }) => {
  const discount = specialPrice ? Math.round(((price - specialPrice) / price) * 100) : 0;

  return (
    <div className="flex items-baseline gap-4">
      {specialPrice ? (
        <>
          <span className="text-3xl font-bold text-gray-900">€{specialPrice.toFixed(2)}</span>
          <span className="text-xl text-gray-500 line-through">€{price.toFixed(2)}</span>
          <span className="text-lg font-medium text-green-600">{discount}% off</span>
        </>
      ) : (
        <span className="text-3xl font-bold text-gray-900">€{price.toFixed(2)}</span>
      )}
    </div>
  );
};