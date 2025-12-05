from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import json
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================
# TEMPLATES + STATIC FILES
# ===========================
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# ===========================
# 1. Pydantic Model
# ===========================
class PredictionForm(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# ===========================
# 2. Load Model + Scaler + Features
# ===========================
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_PATH, "models", "model.pkl"))
scaler = joblib.load(os.path.join(BASE_PATH, "models", "scaler.pkl"))

with open(os.path.join(BASE_PATH, "models", "features.json"), "r") as f:
    feature_names = json.load(f)

# ===========================
# 3. Routes
# ===========================
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: PredictionForm):
    input_list = [getattr(data, feat) for feat in feature_names]
    input_array = np.array(input_list).reshape(1, -1)
    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)[0]
    return {"prediction": int(prediction)}

@app.post("/predict_form")
def predict_form(data: PredictionForm):
    input_list = [getattr(data, feat) for feat in feature_names]
    input_array = np.array(input_list).reshape(1, -1)
    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)[0]

    return {
        "prediction": int(prediction),
        "meaning": "1 = Fraud, 0 = Not Fraud"
    }


   


