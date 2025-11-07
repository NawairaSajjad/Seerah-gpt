from flask import Flask, render_template, request, jsonify
from seerah_bot import get_response  # your Python file that handles embeddings & responses

app = Flask(__name__)

# Home / Splash page
@app.route('/')
def index():
    return render_template('index.html')

# Chat page
@app.route('/chat')
def chat():
    return render_template('chat.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# FAQ page
@app.route('/faq')
def faq():
    return render_template('faq.html')

# API endpoint for chat
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get("question", "")
    if user_input:
        bot_response = get_response(user_input)
        return jsonify({"response": bot_response})
    return jsonify({"response": "Please ask a valid question."})

if __name__ == '__main__':
    app.run(debug=True)
