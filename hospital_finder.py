import requests
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("AIzaSyAJtVIIOXfwtC4QO1O-T7jpPj4BPzlwEk8")

def find_nearby_hospitals(lat, lon):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lon}",
        "radius": 5000,
        "type": "hospital",
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    hospitals = []
    for place in data.get("results", []):
        hospitals.append({
            "name": place.get("name"),
            "address": place.get("vicinity", "Address not available")
        })

    return hospitals
