#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import uvicorn
from fastapi import FastAPI
import pickle
import numpy as np
from Diabetes import diabetes


# In[3]:


rf = pickle.load(open('diabetes_classifier.pkl', 'rb'))


# In[4]:


#creating the app
app = FastAPI()

#get the index route
@app.get('/')
def home():
    return {"Welcome to the diabetes classifier"}

@app.post('/predict')
def predict(data:diabetes):
    data = data.dict()
    Pregnancies = data['Pregnancies']
    Glucose = data['Glucose']
    BloodPressure = data['BloodPressure']
    SkinThickness = data['SkinThickness']
    Insulin = data['Insulin']
    BMI = data['BMI']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
    Age = data['Age']
    prediction = rf.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if prediction == 0:
        prediction = "You don't have Diabetes"
    else:
        prediction = "You are having diabetes"
    return {prediction}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload


# In[ ]:




