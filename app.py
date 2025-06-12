from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from main import init_chatbot, get_response

app = Flask(__name__)
CORS(app)  # 👈 Enable CORS for all routes

chatbot = init_chatbot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Please provide a message."}), 400

    try:
        reply = get_response(chatbot, user_message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
