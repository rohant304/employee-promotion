import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# expreinace
X=np.array([
    [1],
    [2],
    [3],
    [4]
    
])

# 0 = not promotion ,1 = promotion
y=np.array([
    0,
    0,
    1,
    1
    
])

model = DecisionTreeClassifier()
model.fit(X,y)

os.makedirs("model",exist_ok=True)

joblib.dump(model,"model/model.pkl")
print("Model Trained Successfully")

