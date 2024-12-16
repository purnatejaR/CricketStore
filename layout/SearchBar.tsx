import React, { useState, useEffect } from 'react';
import { Search } from 'lucide-react';
import { useSearchStore } from '../../store/searchStore';
import { searchProducts } from '../../services/api'; 
import { Link } from 'react-router-dom';

export const SearchBar: React.FC = () => {
  const { setSearchQuery } = useSearchStore();
  const [localQuery, setLocalQuery] = useState('');
  const [searchResults, setSearchResults] = useState<any[]>([]); 

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    setSearchQuery(localQuery);
  };

  useEffect(() => {
    const fetchSearchResults = async () => {
      if (localQuery) {
        try {
          const response = await searchProducts(localQuery); 
          setSearchResults(response.data.products);
        } catch (error) {
          console.error('Failed to fetch search results', error);
        }
      } else {
        setSearchResults([]); 
      }
    };

    const debounceFetch = setTimeout(() => {
      fetchSearchResults();
    }, 300); 

    return () => clearTimeout(debounceFetch); 
  }, [localQuery]);

  const handleResultClick = (productId: string) => {
    setLocalQuery(''); 
    setSearchResults([]); 
    setSearchQuery(localQuery); 
  };

  return (
    <form onSubmit={handleSearch} className="w-full">
      <div className="relative">
        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <Search className="h-5 w-5 text-gray-400" />
        </div>
        <input
          type="text"
          value={localQuery}
          onChange={(e) => setLocalQuery(e.target.value)}
          className="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          placeholder="Search products..."
        />
        {searchResults.length > 0 && (
          <div className="absolute z-10 bg-white border border-gray-300 rounded-md mt-1 w-full">
            {searchResults.map((product) => (
              <Link
                key={product.id}
                to={`/product/${product.id}`} 
                className="block px-4 py-2 text-gray-700 hover:bg-gray-100"
                onClick={() => handleResultClick(product.id)} 
              >
                {product.product_name}
              </Link>
            ))}
          </div>
        )}
      </div>
    </form>
  );
};
