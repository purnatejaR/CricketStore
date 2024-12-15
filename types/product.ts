export interface Product {
  id: string;
  product_name: string;
  product_description: string;
  category: string;
  price: number;
  special_price: number;
  is_available: boolean;
  product_urls: string[];
}

export interface ProductResponse {
  data: Product;
  message: string | null;
  status: string;
}

export interface ProductsListResponse {
  data: {
    products: Product[];
    total_pages?: number;
    current_page?: number;
  };
  message: string | null;
  status: string;
}

export interface CartResponse {
  data: {
    cart: Product[];
  };
  message: string | null;
  status: string;
}