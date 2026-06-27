import joblib

model=joblib.load("model/model.pkl")

experiance= [[1]]

prediction = model.predict(experiance)

if prediction[0] == 1:
    print("promotion")
    
else:
    print("not promotion")
