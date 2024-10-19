from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
import numpy as np

loaded_model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Feature list [T,TM,Tm,H,VV,V,VM]
    features = []
    for i in range(1, 8):  # for 7 features
        features.append(float(request.form[f'feature{i}']))
    
    # Convert features to numpy array and reshape for prediction
    final_features = np.array(features)
    
    # Make prediction
    my_prediction = loaded_model.predict([final_features])
    
    return render_template('result1.html', prediction=[my_prediction[0]])

    # df = pd.read_csv('Final_dataset.csv')
    # my_prediction = loaded_model.predict(df.iloc[:, :-1].values)
    # my_prediction = my_prediction.tolist()
    # return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)