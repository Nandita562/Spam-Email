from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        email_text = data.get('email', '')

        if not email_text:
            return jsonify({'error': 'Empty email text'}), 400

        # Dummy prediction logic (replace with your trained model)
        prediction = "spam" if "win" in email_text.lower() else "not spam"

        return jsonify({'prediction': prediction})
    except Exception as e:
        print("Server Error:", e)
        return jsonify({'error': 'Prediction failed'}), 500

if __name__ == "__main__":
    app.run(debug=True)
