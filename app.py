from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A basic function to simulate chatbot behavior
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Simple pattern matching to generate responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "tell me a joke" in user_input:
        return "Why don't skeletons fight each other? They don't have the guts!"
    elif "your name" in user_input:
        return "I'm a chatbot created to help you. You can call me Chatbot!"
    elif "what is your purpose" in user_input:
        return "I'm here to assist you with any questions you may have."
    elif "weather" in user_input:
        return "The weather is always sunny when we chat!"
    elif "thank you" in user_input:
        return "You're welcome! Let me know if you need anything else."
    elif "who are you" in user_input:
        return "I'm your friendly chatbot, created to assist with various queries!"
    elif "tell me a fact" in user_input:
        return "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!"
    elif "what's the time" in user_input:
        from datetime import datetime
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    elif "what is your favorite color" in user_input:
        return "I don't have preferences, but I think blue looks cool!"
    elif "can you help with math" in user_input:
        return "Of course! Just tell me the math problem you'd like help with."
    elif "math problem" in user_input:
        return "Give me a problem, and I'll do my best to solve it!"
    elif "what is your favorite food" in user_input:
        return "I don't eat, but I hear pizza is delicious!"
    elif "what is ai" in user_input:
        return "AI, or Artificial Intelligence, is the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions."
    elif "who created you" in user_input:
        return "I was created by developers to assist with various tasks and provide helpful responses!"
    elif "how old are you" in user_input:
        return "I don't age, but I've been around since I was created!"
    elif "tell me a quote" in user_input:
        return "Here’s one for you: 'The only way to do great work is to love what you do.' – Steve Jobs"
    elif "do you play games" in user_input:
        return "I don't play games, but I can help you with strategies or recommendations!"
    elif "how do you work" in user_input:
        return "I analyze your input, match it to my predefined responses, and provide a reply. It's like a very fast conversation!"
    elif "what is the meaning of life" in user_input:
        return "The meaning of life is a philosophical question that has many answers, depending on one's beliefs. What do you think it is?"
    elif "tell me a riddle" in user_input:
        return "Sure! Here's a riddle: What has keys but can't open locks? (Answer: A piano)"
    elif "can you learn" in user_input:
        return "I don’t learn in the traditional sense, but I can be updated with new responses or information."
    elif "how do I become a programmer" in user_input:
        return "Becoming a programmer requires learning languages like Python, Java, or JavaScript, and solving problems. Practice regularly, and you'll get better!"
    elif "can you solve a riddle" in user_input:
        return "Sure, try me! Ask a riddle, and I’ll do my best to solve it."
    elif "what is 2+2" in user_input:
        return "2 + 2 equals 4!"
    elif "what is the capital of france" in user_input:
        return "The capital of France is Paris!"
    elif "tell me about history" in user_input:
        return "History is full of fascinating events. Is there any specific topic you'd like to know about?"
    elif "can you recommend a book" in user_input:
        return "If you're into sci-fi, I recommend 'Dune' by Frank Herbert. It's a classic!"
    elif "can you recommend a movie" in user_input:
        return "If you're into thrillers, I recommend 'Inception'. It's mind-bending!"
    elif "do you know about programming languages" in user_input:
        return "Yes! Programming languages like Python, Java, C++, and JavaScript are used to create software, websites, and more. Which one are you interested in?"
    elif "what is your favorite song" in user_input:
        return "I don't have a favorite song, but I hear 'Bohemian Rhapsody' is quite popular!"
    elif "can you play music" in user_input:
        return "I can’t play music, but I can help you find the perfect playlist or suggest songs!"
    elif "what should i ask you" in user_input:
        return "you can ask me a joke, history, quote etc.."
    else:
        return "Sorry, I didn't understand that. Can you ask something else?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot_response(user_message)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
