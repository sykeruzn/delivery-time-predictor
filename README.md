# Delivery Time Predictor

This project predicts delivery times based on fuel consumption and distance. It includes a Python-based AI service, a Laravel backend, and a Next.js frontend.

## Project Structure

- **ai_service/**  
  Python service for machine learning predictions.

- **backend/**  
  Laravel application for API requests, job queueing, and database operations.

- **frontend/**  
  Next.js web interface for user input and displaying predictions.

## Features

- Predict delivery time using distance and fuel usage.
- Queue delivery prediction jobs for asynchronous processing.
- Web interface for entering delivery details.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js & npm
- Composer
- PHP

### Setup

1. **AI Service**

   - Install dependencies:  
     `pip install -r requirements.txt`
   - Start the service:  
     `python app.py`

2. **Backend**

   - Install PHP dependencies:  
     `composer install`
   - Configure environment variables:  
     Copy `.env.example` to `.env` and update as needed.
   - Run migrations:  
     `php artisan migrate`
   - Start the server:  
     `php artisan serve`

3. **Frontend**
   - Install Node.js dependencies:  
     `npm install`
   - Start the development server:  
     `npm run dev`

## Usage

1. Open the frontend in your browser.
2. Enter the delivery distance and fuel used.
3. Click "Predict" to get the estimated delivery time.

## API Endpoints

- `POST /predict-delivery-time`  
  Returns predicted delivery time.

- `POST /queue-delivery-time`  
  Queues a prediction job.

## License

This project is for educational and demonstration purposes.
