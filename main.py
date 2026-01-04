from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Important for Streamlit

app = FastAPI() # <--- THIS IS THE MISSING PART

# This part allows your Streamlit website to talk to your FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "VocalCare API is running"}

@app.get("/hospitals")
def get_hospitals(lat: float, lon: float):
    # Your hospital logic here
    return {"message": f"Searching near {lat}, {lon}"}