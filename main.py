from fastapi import FastAPI
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from pydantic import BaseModel
import numpy as np
import os
app = FastAPI()

# Load Iris data
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict_iris(features: IrisFeatures):
    features_array = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    prediction = model.predict(features_array)
    return {"class": iris.target_names[prediction[0]]}
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to port 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
