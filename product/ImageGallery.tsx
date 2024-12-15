import React, { useState } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import { API_URL } from '../../constants';
interface ImageGalleryProps {
  images: string[];
  productName: string;
}

export const ImageGallery: React.FC<ImageGalleryProps> = ({ images, productName }) => {
  const [currentImage, setCurrentImage] = useState(0);

  const nextImage = () => {
    setCurrentImage((prev) => (prev + 1) % images.length);
  };

  const previousImage = () => {
    setCurrentImage((prev) => (prev - 1 + images.length) % images.length);
  };

  return (
    <div className="relative">
      <div className="aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-lg bg-gray-200">
        <img
          // src={`${API_URL}${images[currentImage].replace('./app/', '')}`}
          src={`${images[currentImage]}`}
          alt={`${productName} - Image ${currentImage + 1}`}

          className="h-full w-full object-cover object-center"
        />
      </div>
      
      {/* Navigation buttons */}
      <button
        onClick={previousImage}
        className="absolute left-2 top-1/2 -translate-y-1/2 bg-white/80 p-2 rounded-full shadow-lg hover:bg-white"
      >
        <ChevronLeft className="w-6 h-6" />
      </button>
      <button
        onClick={nextImage}
        className="absolute right-2 top-1/2 -translate-y-1/2 bg-white/80 p-2 rounded-full shadow-lg hover:bg-white"
      >
        <ChevronRight className="w-6 h-6" />
      </button>

      {/* Thumbnail strip */}
      <div className="mt-4 grid grid-cols-5 gap-2">
        {images.map((image, index) => (
          <button
            key={index}
            onClick={() => setCurrentImage(index)}
            className={`relative aspect-w-1 aspect-h-1 overflow-hidden rounded-md ${
              currentImage === index ? 'ring-2 ring-indigo-500' : ''
            }`}
          >
            <img
              src={`${image}`}
              alt={`${productName} - Thumbnail ${index + 1}`}
              className="h-full w-full object-cover object-center"
            />
          </button>
        ))}
      </div>
    </div>
  );
};