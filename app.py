from flask import Flask, request, render_template
import joblib
import pickle

app = Flask(__name__)

model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    transformed = vectorizer.transform([message])
    prediction = model.predict(transformed)
    result = "HAM" if prediction[0] == 1 else "SPAM"
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
