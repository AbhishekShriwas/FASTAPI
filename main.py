from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the pre-trained Iris model
with open("./Model/R2.pkl", "rb") as fileobj:
    iris_model = pickle.load(fileobj)

# Create the FastAPI app
app = FastAPI()


# Root route
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Request body model for flower features
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Prediction route
@app.post("/predict")
async def predict_iris(features: IrisFeatures):
    input_data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]

    prediction = iris_model.predict(input_data)
    flower_type = int(prediction[0])  # Convert numpy.int64 to int if needed

    return {"prediction": flower_type}

