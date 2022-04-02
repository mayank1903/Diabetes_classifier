#!/usr/bin/env python
# coding: utf-8

# In[5]:


#pydantic is equivalent to the request package
from pydantic import BaseModel


# In[6]:


class diabetes(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# In[ ]:




