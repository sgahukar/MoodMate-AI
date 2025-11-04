# app.py
from flask import Flask, render_template, request
from utils.detect_emotion import predict_emotion
from utils.response_generator import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_text = request.form['user_text']
    emotion = predict_emotion(user_text)
    response = generate_response(emotion)
    return render_template('result.html', text=user_text, emotion=emotion, response=response)

if __name__ == '__main__':
    app.run(debug=True)
