from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load models
with open('C:\\Users\\User\\Downloads\\Model Development\\RF.pkl', 'rb') as f:
    clf = pickle.load(f)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Corrected template name


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = clf.predict(final_features)
    output = round(prediction[0], 2)
    if output == 0:  # Corrected indentation
        # Pass the prediction result to the HTML template for rendering
        return render_template('index.html', prediction_text='Transaction is authentic.')
    else:
        return render_template('index.html', prediction_text='Transaction is fraudulent.')

if __name__ == '__main__':
    app.run(debug=True)
