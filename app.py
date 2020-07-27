# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np


classifier = pickle.load(open('house_price6.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        location = int(request.form['location'])
        Squareft = int(request.form['Squareft'])
        Bathrooms = int(request.form['Bathrooms'])
        Bhk = int(request.form['Bhk'])


        data = np.array([[location,Squareft,Bathrooms,Bhk]])
        prediction = classifier.predict(data)

        output = round(prediction[0], 2)


        return render_template('index.html',prediction_texts=" You Can Buy House At {} Lakhs".format(output))





if __name__ == '__main__':
    app.run(debug=True)