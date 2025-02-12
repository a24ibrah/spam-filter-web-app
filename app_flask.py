from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('spam_filter_model.pkl')

@app.route('/classify', methods=['POST'])
def classify_email():
    data = request.json
    email_text = data.get('email_text', '')

    # Predict using the model
    prediction = model.predict([email_text])
    result = 'spam' if prediction[0] == 1 else 'ham'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)