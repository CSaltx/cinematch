from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


from api_call import develop_response

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Set CORS for all routes


@app.route('/recommend', methods=['POST'])
@cross_origin(origins=["http://localhost:3000"])  # Allow only the specific origin
def recommend():
    # Extract the message from the POST request
    data = request.json
    message = data.get('message')
    
    # Check if the message is provided
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    # Use the existing code to get a response from the OpenAI API
    response_text = develop_response(script=[], message=message)

    # Return the response in JSON format
    return jsonify({'response': response_text})


@app.route('/health', methods=['GET'])
@cross_origin()
def health_check():
    return jsonify({'status': 'up'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)