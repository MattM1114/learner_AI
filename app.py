from flask import Flask, jsonify, request
from chatbot import chat  # Ensure this imports your chat function correctly
from flask_cors import CORS  # Import CORS if you're serving the frontend from a different origin
from waitress import serve


app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes
serve(app, host='0.0.0.0', port=8080)

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    response = chat(query)  # Call your chatbot function with the user query
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

