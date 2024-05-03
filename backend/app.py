from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
# model = joblib.load("")  # Replace "your_model.pkl" with your model file

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/predict', methods=['POST'])
'''
def predict():
    if request.method == 'POST':
        input_data = request.form.to_dict()
        df = pd.DataFrame(input_data, index=[0])
        prediction = model.predict(df)[0]
        return render_template('result.html', prediction=prediction)
        '''

if __name__ == '__main__':
    app.run(debug=True)
