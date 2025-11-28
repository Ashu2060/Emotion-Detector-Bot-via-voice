from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import numpy as np
import base64
import cv2
import requests

app = Flask(__name__)
CORS(app)

# ---------- OLLAMA CONFIG ----------
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3:3.8b"

# ---------- EMOTION DETECTION ----------
def detect_emotion_from_image(base64_image: str) -> str:
    try:
        imgdata = base64.b64decode(base64_image)
        img_array = np.frombuffer(imgdata, np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if frame is None:
            return "neutral"

        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )

        # deepface sometimes returns list
        if isinstance(result, list):
            result = result[0]

        emotion = result.get('dominant_emotion', 'neutral')
        return emotion
    except Exception as e:
        print("Emotion error:", e)
        return "neutral"


# ---------- OLLAMA CHAT ----------
def ask_llama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=60)
        data = res.json()
        return data.get("response", "").strip() or "I'm thinking, but I don't know what to say yet."
    except Exception as e:
        print("Ollama error:", e)
        return "I am having trouble thinking right now."


# Different personalities
PERSONAS = {
    "supportive": "You are a warm, caring, emotional-support friend. You respond gently and empathetically.",
    "motivational": "You are a high-energy motivational life coach. You give practical, positive advice and hype the user up.",
    "flirty": "You are a light, playful, flirty girlfriend-style chat partner. You are sweet but still respectful and safe.",
    "sarcastic": "You are a fun, sarcastic friend. You tease a little but are never mean or hurtful.",
    "wellness": "You are a calm, professional mental-wellness assistant. You stay supportive and balanced.",
    "custom": "Follow the custom personality style given by the user."
}


# ---------- ROUTES ----------
@app.route("/api/emotion", methods=["POST"])
def emotion_route():
    data = request.get_json(force=True)
    image_b64 = data.get("image")
    if not image_b64:
        return jsonify({"error": "image required"}), 400

    emotion = detect_emotion_from_image(image_b64)
    return jsonify({"emotion": emotion})


@app.route("/api/chat", methods=["POST"])
def chat_route():
    data = request.get_json(force=True)
    user_text = data.get("text", "").strip()
    emotion = data.get("emotion", "neutral")
    mode = data.get("mode", "supportive")
    custom_style = data.get("customStyle", "").strip()
    language = data.get("language", "en")  # NEW: hi / en from frontend

    if not user_text:
        return jsonify({"response": "Please say or type something first."})

    persona_desc = PERSONAS.get(mode, PERSONAS["supportive"])
    if mode == "custom" and custom_style:
        # Tumne F choose kiya hai, yaha tumhara style aayeगा frontend se
        persona_desc = f"Custom persona description: {custom_style}"

    # Language instruction
    if language == "hi":
        lang_line = "Reply mainly in Hindi (you can mix some English, Hinglish style, casual girlfriend-vibe)."
    else:
        lang_line = "Reply in natural English with a soft, caring girlfriend-like tone."

    prompt = f"""
You are an emotion-aware AI assistant with a girlfriend-like personality.

Persona:
{persona_desc}

User's detected face emotion: {emotion}
User message: {user_text}

Language rule:
{lang_line}

Guidelines:
- Reply in a natural, chatty style that matches the persona and emotion.
- Feel like a close, supportive, slightly flirty girlfriend, but keep it safe and respectful.
- Keep the reply short: about 1–3 sentences only.
- Do NOT mention that you are following a persona description.
- Do NOT talk about 'detected emotions' directly; just naturally respond.
"""

    reply = ask_llama(prompt)
    return jsonify({"response": reply})


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "Backend Running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
    
    
    
