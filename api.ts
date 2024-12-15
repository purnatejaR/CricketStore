import axios from 'axios';
import { LoginCredentials, RegisterCredentials, AuthResponse } from '../types/auth';
import { ProductResponse, ProductsListResponse, CartResponse } from '../types/product';
import { API_URL } from '../constants';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests if it exists
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth-storage');
  
  if (token) {
    const parsedToken = JSON.parse(token).state.token;
    if (parsedToken){
      console.log('Sending token:', parsedToken.access_token);
      config.headers.Authorization = `Bearer ${parsedToken.access_token}`;
    }
  }
  return config;
});

export const login = async (credentials: LoginCredentials): Promise<AuthResponse> => {
  const response = await api.post<AuthResponse>('/auth/login', credentials);
  return { access_token: response.data.data };
};

export const register = async (credentials: RegisterCredentials): Promise<AuthResponse> => {
  const response = await api.post<AuthResponse>('/auth/register', credentials);
  return response.data;
};

export const getProduct = async (productId: string): Promise<ProductResponse> => {
  const response = await api.get<ProductResponse>(`/api/products/${productId}`);
  return response.data;
};

export const getProducts = async (page: number = 1, perPage: number = 10): Promise<ProductsListResponse> => {
  const response = await api.get<ProductsListResponse>(`/api/products?page=${page}&per_page=${perPage}`);
  return response.data;
};

export const getCart = async (): Promise<CartResponse> => {
  const response = await api.get('/api/cart');
  return response.data;
};

export const removeFromCart = async (productId: string): Promise<any> => {
  await api.delete('/api/cart', { data: { product_id: productId } });
};

export const addToCart = async (productId: string): Promise<any> => {
  await api.post('/api/cart', { product_id: productId });
};

export const getOrders = async (): Promise<any> => {
  const response = await api.get('/api/orders');
  return response.data;
};

export const placeOrder = async (productIds: string[], address: any): Promise<any> => {
  await api.post('/api/order', { product_ids: productIds, address });
};

export const searchProducts = async (query: string): Promise<any> => {
  const response = await api.get(`/api/search?q=${query}`);
  return response.data;
};