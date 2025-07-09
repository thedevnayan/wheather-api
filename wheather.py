# filename: dummy_weather_api.py

from fastapi import FastAPI, Query

# Create FastAPI app
app = FastAPI()

# Dummy weather data (pretend database)
dummy_weather_data = {
    "London": {"temperature": 20, "humidity": 60, "description": "Partly cloudy"},
    "New York": {"temperature": 25, "humidity": 55, "description": "Sunny"},
    "Udaipur": {"temperature": 30, "humidity": 40, "description": "Hot and dry"},
}

@app.get("/")
def root():
    return {"message": "Dummy Weather API: Use /weather?location=London"}

@app.get("/weather")
def get_weather(location: str = Query(..., description="City name")):
    """
    Return dummy weather data for the given location.
    Example: /weather?location=London
    """
    weather = dummy_weather_data.get(location)
    if weather:
        return {
            "location": location,
            "weather": weather
        }
    else:
        return {
            "error": f"No weather data found for '{location}'. Try: London, New York, or Udaipur."
        }
