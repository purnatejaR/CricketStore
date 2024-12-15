import React from 'react';

interface ProductHeaderProps {
  name: string;
  category: string;
}

export const ProductHeader: React.FC<ProductHeaderProps> = ({ name, category }) => {
  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900">{name}</h1>
      <div className="mt-2">
        <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800">
          {category}
        </span>
      </div>
    </div>
  );
};