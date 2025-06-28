# 🧘‍♀️ AI Mood-Based Sanskrit Mantra App

This is a simple yet powerful web application that uses **AI sentiment analysis** to understand your current emotional state and recommends a personalized **Sanskrit mantra**, complete with dynamic audio chanting.

Built with **Streamlit**, powered by **Hugging Face Transformers** for emotion detection, and uses **gTTS** to generate mantra chanting in near-Sanskrit pronunciation.

---

## ✨ Features

- 🔍 **AI-driven emotion detection** from natural language input
- 🎯 Maps detected sentiment to one of 14 emotions (joy, sadness, anger, fear, anxiety, stress, gratitude, love, loneliness, compassion, confidence, surprise, disgust, neutral)
- 📜 Fetches a relevant **Sanskrit mantra**, with transliteration, meaning, and explanation from a local SQLite database
- 🎧 Dynamically generates mantra chanting audio with Google Text-to-Speech
- 🖥 Deployed easily on **Streamlit Cloud** or **Hugging Face Spaces**

---

## 🚀 How to Run Locally

Clone this repository and install the required Python packages:

```bash
git clone https://github.com/yourusername/ai-mood-mantra-app.git
cd ai-mood-mantra-app
pip install -r requirements.txt
Then run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
🌐 How to Deploy
✅ Streamlit Cloud
Push your code to a GitHub repository.

Go to https://streamlit.io/cloud and sign in with GitHub.

Click “New app”, select your repo and app.py, and deploy.

✅ Hugging Face Spaces
Create a new Space (it auto-detects Streamlit).

Upload app.py, requirements.txt, and mantras.db.

Hugging Face will automatically install dependencies and host your app.

💡 Example Inputs
Try entering sentences like:

I feel anxious about tomorrow and need something to calm my mind.

I am so happy today, everything feels wonderful!

I feel really alone right now, like nobody understands me.

I want to be more compassionate toward others.

The app will detect your emotion and guide you with a fitting Sanskrit mantra.

🏗 Tech Stack
Streamlit — simple and elegant web interface

Hugging Face Transformers — for sentiment analysis

SQLite — lightweight local database for mantras

gTTS — dynamic text-to-speech chanting

Torch — powering the transformer models

🚀 Future Scope
This project is designed to be a foundation for blending ancient Sanskrit wisdom with modern AI. Future enhancements could include:

🎤 Human-like TTS or professional Sanskrit recordings for more authentic mantra chanting

🌍 Multi-language support for meaning & explanations (e.g. Hindi, Tamil, English side-by-side)

📈 Tracking mood over time to visualize emotional health patterns

🙌 Integration with meditation timers or guided breathing modules

🧘 Personalized mantra playlists based on repeated moods

☁️ Option to store user history securely (with privacy-focused cloud DB)

🤖 Using advanced emotion detection models that recognize compound emotions (like joy + anxiety)

🙏 License
MIT License — open for learning, remixing, and building new mindfulness tools.
