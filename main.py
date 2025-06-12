import google.generativeai as genai

API_KEY = "AIzaSyBEubfmiQhpiSaMLm0i119Xi22XEgbH12U"

def init_chatbot():
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=(
            "You are a compassionate, supportive mental health chatbot. "
            "Always respond in a calming, non-judgmental, and empathetic tone. "
            "Offer encouragement, emotional support, helpful tips for self-care, "
            "and suggest breathing exercises or affirmations if needed. "
            "Avoid giving medical diagnoses or professional therapy advice, but always listen patiently. "
            "Use emojis when appropriate to express empathy, care, or positivity."
        )
    )
    chat = model.start_chat(history=[])
    return chat

def enhance_with_emojis(text):
    emoji_map = {
        "anxious": "😟",
        "anxiety": "😰",
        "depressed": "😔",
        "sad": "😢",
        "stress": "😓",
        "overwhelmed": "😫",
        "panic": "🚨",
        "breathe": "🧘‍♂️",
        "relax": "😌",
        "calm": "🌿",
        "strong": "💪",
        "capable": "🦸",
        "hope": "🌈",
        "happy": "😊",
        "proud": "🥹",
        "focus": "🎯",
        "peace": "☮️",
        "safe": "🛡️",
        "support": "🤝",
        "courage": "🦁",
    }
    for word, emoji in emoji_map.items():
        if word in text.lower():
            text += f" {emoji}"
    return text

def get_response(chat, user_input):
    response = chat.send_message(user_input)
    raw_response = response.text
    return enhance_with_emojis(raw_response)