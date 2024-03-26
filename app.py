from flask import Flask, jsonify, request
from chatbot import chat  # Import your chatbot function from the existing Python code

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    response = chat(query)  # Call your chatbot function with the user query
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
