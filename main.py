from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

WEATHER_API_KEY = "cda257269cd8f052e74dc19afdd5252c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
def get_weather(city: str):
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="City not found")
    
    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
