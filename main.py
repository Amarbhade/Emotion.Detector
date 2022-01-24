from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model=pickle.load(open("emotions","rb"))
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/predict',methods=["POST"])
def predict():
    text=request.form.get("text")
    result=model.predict([text])[0]
    return render_template("index.html",prediction_text=" THE EMOTION IN TEXT IS  ( {} )".format(result))

if __name__ == "__main__":
    app.run(debug=True)