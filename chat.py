from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize the chatbot
chatbot = ChatBot('PythonBot')

# Set up the chatbot's training
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    user_input = request.args.get('msg')
    return jsonify({"response": str(chatbot.get_response(user_input))})

if __name__ == "__main__":
    app.run(debug=True)
