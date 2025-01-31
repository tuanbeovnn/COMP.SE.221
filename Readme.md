# Weather Microservice

## Overview
This is a Python-based microservice built using FastAPI that fetches weather data for a given city using the OpenWeatherMap API.

## Features
- Fetches real-time weather data for any city.
- Uses FastAPI for efficient performance.
- Securely handles API keys via environment variables.
- Returns JSON responses with city name, temperature, and weather description.

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- Requests
- Python-dotenv

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/weather-microservice.git
   cd weather-microservice
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your OpenWeatherMap API key:
   ```
   WEATHER_API_KEY=your_openweathermap_api_key
   ```
4. Run the service:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
To fetch weather data for a city, use the following endpoint:
```bash
GET /weather/{city}
```
Example:
```bash
curl http://127.0.0.1:8000/weather/London
```

## License
This project is open-source and available under the MIT License.

