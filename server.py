from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():

    data = request.json
    user = data["text"]

    print(user)

    reply = "Hello from Moly Cloud 😄"

    return jsonify({
        "reply": reply
    })

@app.route('/')
def home():
    return "Moly Server Running"