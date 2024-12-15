import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ShoppingCart, LogOut, Search, Grid } from 'lucide-react';
import { useAuthStore } from '../../store/authStore';
import { SearchBar } from './SearchBar';

export const Navbar: React.FC = () => {
  const navigate = useNavigate();
  const clearToken = useAuthStore((state) => state.clearToken);

  const handleLogout = () => {
    localStorage.removeItem('auth-storage');
    localStorage.clear();
    console.log(localStorage);
    clearToken();
    navigate('/login');
  };

  return (
    <nav className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex-shrink-0">
            <Link to="/products" className="flex items-center">
              <Grid className="h-8 w-8 text-indigo-600" />
              <span className="ml-2 text-xl font-bold text-gray-900">EShop</span>
            </Link>
          </div>

          <div className="flex-1 max-w-2xl mx-8">
            <SearchBar />
          </div>

          <div className="flex items-center">
            <Link to="/cart" className="mr-4">
              <ShoppingCart className="h-6 w-6 text-indigo-600" />
            </Link>
            <Link to="/orders" className="mr-4">
              <span className="text-indigo-600">Orders</span>
            </Link>
            <button
              onClick={handleLogout}
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              <LogOut className="h-4 w-4 mr-2" />
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};