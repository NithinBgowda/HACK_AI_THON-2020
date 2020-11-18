from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('forest.html')

@app.route('/predict', methods = ['POST'])
def result():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    ar = np.array([[data1, data2, data3]])
    p = model.predict(ar)
    return render_template('prediction.html', data=p)
if __name__ == "__main__":
    app.run(debug=True)
