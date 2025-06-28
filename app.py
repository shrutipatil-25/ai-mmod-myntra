
import streamlit as st
import sqlite3
from transformers import pipeline
from gtts import gTTS
import tempfile

# Load sentiment model
classifier = pipeline("sentiment-analysis")

# Map sentiment to emotion
def map_sentiment(sentiment):
    if sentiment == "POSITIVE":
        return "joy"
    elif sentiment == "NEGATIVE":
        return "sadness"
    else:
        return "neutral"

# Fetch mantra from DB
def get_mantra(emotion):
    conn = sqlite3.connect("mantras.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mantras WHERE emotion=?", (emotion,))
    result = cur.fetchone()
    conn.close()
    return result

# Generate audio with gTTS
def generate_audio(text):
    try:
        tts = gTTS(text, lang='hi')
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_audio.name)
        return temp_audio.name
    except Exception as e:
        st.error(f"Audio generation failed: {e}")
        return None

# Streamlit UI
st.set_page_config(page_title="AI Sanskrit Mantra App", page_icon="🧘‍♀️")
st.title("🧘‍♀️ Sanskrit Mantra Recommender")
st.markdown("Describe how you're feeling, and receive a personalized Vedic mantra with audio.")

st.markdown("💡 *Example:* `I feel anxious about tomorrow and need something to calm my mind.`")

use_demo = st.button("Use Demo Input")
if use_demo:
    user_input = "I feel anxious about tomorrow and need something to calm my mind."
else:
    user_input = st.text_area("🗣 How do you feel right now?", value="", height=100)

if st.button("🔮 Get My Mantra"):
    if not user_input.strip():
        st.warning("⚠️ Please enter something first.")
    else:
        result = classifier(user_input)[0]
        sentiment = result["label"]
        emotion = map_sentiment(sentiment)

        st.success(f"🧠 Detected Sentiment: `{sentiment}` → Emotion: `{emotion}`")

        mantra = get_mantra(emotion)
        if mantra:
            _, sanskrit, translit, meaning, explanation, _ = mantra
            st.markdown(f"### 🙏 Your Mantra")
            st.markdown(f"**📜 Sanskrit:** `{sanskrit}`")
            st.markdown(f"**🔤 Transliteration:** `{translit}`")
            st.markdown(f"**💡 Meaning:** {meaning}")
            st.markdown(f"**🧠 Explanation:** {explanation}")

            audio_path = generate_audio(translit)
            if audio_path:
                st.audio(audio_path)
            else:
                st.warning("Audio playback failed.")
        else:
            st.error("❌ No mantra found for this emotion.")
