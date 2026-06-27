from flask import Flask

import joblib

app = Flask(__name__)

model = joblib.load("model/model.pkl")

@app.route("/")

def home():
    prediction = model.predict([[1]])
    
    result = "promotion" if prediction[0]==1 else "not promotion"
    
    return f"employee Result:{result}"

if __name__ == "__main__":
    app.run(debug=True)