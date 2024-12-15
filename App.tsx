import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { Products } from './pages/Products';
import { ProductDetail } from './pages/ProductDetail';
import { Cart } from './pages/Cart';
import { Orders } from './pages/Orders';
import { PlaceOrder } from './pages/PlaceOrder';
import { useAuthStore } from './store/authStore';

function App() {
  const token = useAuthStore((state) => state.token);

  return (
    <Router>
      <Toaster position="top-right" />
      <Routes>
        <Route path="/login" element={!token ? <Login /> : <Navigate to="/products" />} />
        <Route path="/register" element={!token ? <Register /> : <Navigate to="/products" />} />
        <Route path="/products" element={token ? <Products /> : <Navigate to="/login" />} />
        <Route path="/product/:productId" element={token ? <ProductDetail /> : <Navigate to="/login" />} />
        <Route path="/cart" element={token ? <Cart /> : <Navigate to="/login" />} />
        <Route path="/orders" element={token ? <Orders /> : <Navigate to="/login" />} />
        <Route path="/placeorder" element={token ? <PlaceOrder /> : <Navigate to="/login" />} />
        <Route path="/" element={<Navigate to={token ? "/products" : "/login"} />} />
      </Routes>
    </Router>
  );
}

export default App;