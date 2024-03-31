from flask import Flask, jsonify, request
from chatbot import chat  # Ensure this imports your chat function correctly
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    response = chat(query)  # Call your chatbot function with the user query
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
