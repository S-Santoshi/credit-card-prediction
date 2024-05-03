from flask import Flask, render_template, request
import pandas as pd
import joblib
import pickle
from dataprocessing import process_data

app = Flask(__name__)



# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = request.form.to_dict()
        print(input_data)
        prediction=process_data(input_data)
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

dummy_input={'gender': 'F', 'property': '1', 'car': '1', 'children': '3', 'income': '123456', 'emplymentStatus': 'Working', 'education': 'Secondary / secondary special', 'maritalStatus': 'Married', 'dwelling': 'With parents', 'age': '28', 'employmentDate': '2022-06-03', 'workPhone': '1', 'phone': '1', 'email': '1', 'jobTitle': 'IT staff', 'familyMemberCount': '3', 'accountAge': '10'}