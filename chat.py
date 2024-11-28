from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A simple function to get predefined responses
def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm good, thank you for asking!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I don't understand that. Can you try again?"
    }
    # Convert user input to lowercase and check for response
    return responses.get(user_input.lower(), responses["default"])

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
