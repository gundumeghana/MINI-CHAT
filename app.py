
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/ai")
def ai():
    return render_template("ai.html")

@socketio.on("message")
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)

@app.route("/api/ai-reply", methods=["POST"])
def ai_reply():
    data = request.get_json()
    user_msg = data.get("message", "").lower()
    responses = {
        "sad": "I'm here for you. Remember, it's okay to feel this way sometimes.",
        "happy": "That's awesome! Keep spreading positivity!",
        "angry": "Take a deep breath. Let’s talk it through calmly.",
        "love": "That’s beautiful! Love makes life meaningful.",
        "default": "Hmm... tell me more about that."
    }
    if any(word in user_msg for word in ["sad", "upset", "down"]):
        reply = responses["sad"]
    elif any(word in user_msg for word in ["happy", "great", "good", "awesome"]):
        reply = responses["happy"]
    elif any(word in user_msg for word in ["angry", "mad", "furious"]):
        reply = responses["angry"]
    elif any(word in user_msg for word in ["love", "crush", "like"]):
        reply = responses["love"]
    else:
        reply = responses["default"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
