💋 Emotion Girlfriend Bot
An AI-powered chatbot that detects your emotions through your webcam and responds with a girlfriend-like personality. The bot adapts its responses based on your facial expressions and can speak in both Hindi/Hinglish and English.

✨ Features
Real-time Emotion Detection: Uses DeepFace to analyze facial expressions from webcam feed
Voice Interaction: Speech-to-text input and text-to-speech output with female voice
Multiple Personalities: Choose from supportive, motivational, flirty, sarcastic, wellness, or create your own custom persona
Bilingual Support: Communicate in English or Hindi/Hinglish
Chat History: View your conversation history with the bot
Flexible Reply Modes: Choose voice-only, text-only, or both
Emotion-Aware Responses: Bot adapts tone and content based on detected emotions
🛠️ Tech Stack
Backend
Flask: Python web framework
DeepFace: Facial emotion recognition
OpenCV: Image processing
Ollama: Local LLM inference (Phi3 model)
Frontend
React: UI framework
Webcam: Video capture
Web Speech API: Voice input/output
📋 Prerequisites
Python 3.8+
Node.js 14+
Ollama installed locally
Webcam access
🚀 Installation
1. Clone the Repository
bash
git clone https://github.com/yourusername/emotion-girlfriend-bot.git
cd emotion-girlfriend-bot
2. Setup Backend
bash
# Install Python dependencies
pip install flask flask-cors deepface opencv-python numpy requests

# Install Ollama (if not already installed)
# Visit: https://ollama.ai/download

# Pull the Phi3 model
ollama pull phi3:3.8b
3. Setup Frontend
bash
# Navigate to frontend directory (if separate)
cd frontend

# Install dependencies
npm install react-webcam

# Install additional dependencies if needed
npm install
🎮 Usage
Start the Backend Server
bash
# Make sure Ollama is running
ollama serve

# In a new terminal, start Flask backend
python app.py
The backend will run on http://localhost:5000

Start the Frontend
bash
# In frontend directory
npm start
The frontend will run on http://localhost:3000

🎭 Available Personalities
Supportive: Warm, caring, emotional-support friend
Motivational: High-energy life coach
Flirty: Light, playful girlfriend-style (default custom setting)
Sarcastic: Fun, teasing friend
Wellness: Professional mental-wellness assistant
Custom: Define your own personality style
🎯 How It Works
Capture Emotion: Click "Detect & Talk" to capture a webcam frame
Emotion Analysis: DeepFace analyzes your facial expression
Generate Response: Your message + detected emotion is sent to Ollama
Adaptive Reply: Bot responds based on emotion, personality, and language preference
Voice Output: Hear the response in a female voice (if enabled)
🔧 Configuration
Backend Settings (app.py)
python
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3:3.8b"  # Change model if needed
Frontend Settings (App.js)
javascript
const BACKEND_URL = "http://localhost:5000";  // Update if backend runs elsewhere
🎨 Customization
Create Your Own Personality
Select "Custom personality" from the dropdown
Describe your desired bot personality in the text area
Example: "A sweet Hindi-English speaking girlfriend who motivates and flirts lightly"
Adjust Voice Settings
The bot automatically selects a female voice from available system voices. You can modify voice parameters in the speak() function:

javascript
utter.rate = 1;      // Speech speed
utter.pitch = 1.1;   // Voice pitch (higher = more feminine)
utter.volume = 1;    // Volume level
🌐 Language Support
English: Natural girlfriend-like tone
Hindi/Hinglish: Casual conversational style with mixed Hindi-English
📱 Features by Mode
Reply Modes
Voice + Text: See and hear responses
Voice Only: Audio responses only
Text Only: Silent text responses
⚠️ Known Limitations
Requires webcam access for emotion detection
Ollama must be running locally
Speech recognition may vary by browser (best in Chrome)
Voice quality depends on system TTS voices
Emotion detection requires good lighting
🔒 Privacy
All processing happens locally on your machine
No data is sent to external servers
Webcam images are processed in real-time and not stored
🐛 Troubleshooting
Backend Issues
Ollama error: Ensure Ollama is running (ollama serve)
Import errors: Install missing Python packages
Port conflicts: Change port in app.run()
Frontend Issues
Webcam not working: Check browser permissions
CORS errors: Verify backend CORS is enabled
Voice not working: Check browser compatibility (Chrome recommended)
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
📄 License
This project is open source and available under the MIT License.

🙏 Acknowledgments
DeepFace for emotion recognition
Ollama for local LLM inference
React Webcam for camera integration
📞 Support
For issues and questions, please open an issue on GitHub.

Note: This is an experimental project for educational purposes. Use responsibly and ensure compliance with local regulations regarding AI and privacy.

