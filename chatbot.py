# Jordan Harmon
# Project 2: Chatbot
# September 21, 2025

from flask import Flask, request, jsonify, render_template
import nltk
from nltk.tokenize import word_tokenize


nltk.download ('punkt', quiet=True)

app = Flask(__name__)

# keywords, responses

INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "hiya", "good morning", "good afternoon"],
        "responses": [
            "Hi there! 🌸 How are you feeling today?",
            "Hello! 🌼 Remember to take things one step at a time.",
            "Hey 👋 How’s your day going?"
        ]
    },
    "stress": {
        "keywords": ["stress", "stressed", "overwhelmed", "tension"],
        "responses": [
            "Try taking 5 deep breaths 🌬️.",
            "A short walk outside can do wonders 🌿.",
            "Write down what’s on your mind — journaling helps release stress ✍️."
        ]
    },
    "anxiety": {
        "keywords": ["anxiety", "anxious", "nervous", "worry", "panic", "uneasy"],
        "responses": [
            "Ground yourself: 5 things you see 👀, 4 you touch ✋, 3 you hear 👂, 2 you smell 👃, 1 you taste 👅.",
            "Listen to calming music 🎶 or try progressive muscle relaxation.",
            "Remember: feelings of anxiety always pass 💙.",
            "Try slow, deep breaths — in for 4, hold for 4, out for 6 🌬️.",
            "Write down your worries and set them aside for now 📝.",
            "Take a short walk outside; fresh air can reduce anxious thoughts 🌿."
        ]
    },
    "sleep": {
        "keywords": ["sleep", "tired", "restless", "insomnia", "nap", "rest"],
        "responses": [
            "Avoid screens 30 minutes before bed 🛌.",
            "Try a relaxing nighttime routine: reading, tea, soft music 🎵.",
            "Keep your room cool, dark, and quiet 🌙.",
            "Stick to a consistent sleep schedule — even on weekends ⏰.",
            "Consider journaling to clear your mind before bed 📝.",
            "Limit caffeine in the afternoon to sleep better ☕️."
        ]
    },
    "exercise": {
        "keywords": ["exercise", "workout", "run", "walk", "gym", "yoga", "stretch"],
        "responses": [
            "Even a 10-minute walk boosts energy 🏃‍♀️.",
            "Stretching for a few minutes can improve circulation 🧘.",
            "Dancing to one song counts as exercise 💃!",
            "Consistency matters more than intensity — small steps count! 👣",
            "Try alternating between cardio and strength exercises for variety 💪.",
            "Remember, exercise also helps reduce stress and improve mood 🌸."
        ]
    },
    "water": {
        "keywords": ["water", "hydrate", "thirsty", "drink", "hydration"],
        "responses": [
            "Hydration check! 💧 Have you had some water today?",
            "Drink a glass of water now — your body will thank you 🚰.",
            "Water helps with focus, mood, and energy ⚡.",
            "Aim to drink at least 8 cups of water a day 💦.",
            "Try keeping a reusable bottle nearby as a reminder 🥤.",
            "Herbal teas count toward hydration too 🌿."
        ]
    },
    "break": {
        "keywords": ["break", "pause", "rest", "timeout", "stretch", "relax"],
        "responses": [
            "Step away from your screen for 5 minutes 🌸.",
            "Stretch your arms and legs 🧘.",
            "Breaks actually make you more productive ⚡.",
            "Take a few moments to breathe deeply and reset 🌬️.",
            "A short walk or tea break can boost creativity ☕️.",
            "Close your eyes for a minute and let your mind rest 💤."
        ]
    },
    "gratitude": {
        "keywords": ["gratitude", "thankful", "thanks", "appreciate", "blessed"],
        "responses": [
            "List 3 things you’re grateful for today 🙏.",
            "Gratitude journaling can shift your mood 💡.",
            "Share one thing you’re thankful for with a friend ❤️.",
            "Try saying out loud one thing you appreciate about yourself 🗣️.",
            "Reflect on a small positive moment from today 🌞.",
            "Even noticing small wins can boost your gratitude mindset 🌸."
        ]
    },
    "default": {
        "keywords": [],
        "responses": [
            "I’m here for you 💙 Try asking about stress, sleep, exercise, or gratitude.",
            "Remember to take care of yourself 🌿.",
            "That’s interesting! Maybe focus on a small act of self-care today ☀️.",
            "I can give tips on sleep, exercise, hydration, mindfulness, or gratitude 🌱.",
            "Remember, self-care is personal — even small steps help 💛."
        ]
    }
}

import random

def get_response(user_input):
    user_input = user_input.lower()
    
    for intent, data in INTENTS.items():  # Loop through each intent
        for keyword in data["keywords"]:  # Check all keywords for that intent
            if keyword in user_input:
                return random.choice(data["responses"])  # Pick a random response
    
    # If no keyword matches, use default
    return random.choice(INTENTS["default"]["responses"])

# app launching

@app.route("/")
def index():
    return render_template("index.html")  # Flask looks in templates/

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)