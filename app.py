import streamlit as st
import pandas as pd
import os
from transformers import pipeline
from datetime import datetime

st.set_page_config(page_title="ProverbHub", layout="centered")

st.title("🌾 ProverbHub: Preserve, Translate, and Celebrate Local Wisdom")
st.caption("Contribute your region's proverbs in your own language and help build a multilingual cultural corpus.")

# Load or initialize the data storage
data_file = "proverbs.csv"
if not os.path.exists(data_file):
    df = pd.DataFrame(columns=["Proverb", "Meaning", "Language", "Region", "Usage", "Date"])
    df.to_csv(data_file, index=False)
else:
    df = pd.read_csv(data_file)

# Load translator pipeline (caches locally)
@st.cache_resource
def load_translation_pipeline():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

translator = load_translation_pipeline()

# --- Input form ---
with st.form("proverb_form"):
    proverb = st.text_area("📝 Proverb (in your language)", max_chars=200)
    meaning = st.text_area("💡 Meaning (in any language)", max_chars=300)
    region = st.text_input("📍 Region (Village/Town/State)")
    language = st.text_input("🗣️ Language (e.g., Telugu, Hindi, Tamil)")
    usage = st.text_area("📚 Usage in a sentence (optional)", max_chars=300)
    submitted = st.form_submit_button("Submit ✨")

    if submitted and proverb.strip() and meaning.strip():
        new_row = {
            "Proverb": proverb.strip(),
            "Meaning": meaning.strip(),
            "Language": language.strip(),
            "Region": region.strip(),
            "Usage": usage.strip(),
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Append new entry
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(data_file, index=False)
        st.success("Thank you for preserving your culture! 🙌")

        # Translate and show English version
        try:
            translated = translator(proverb, max_length=100)[0]['translation_text']
            st.markdown(f"**🗺️ English Translation (AI):** _{translated}_")
        except Exception as e:
            st.warning("Translation failed. Please try again later.")

# --- Display recent submissions ---
st.markdown("---")
st.subheader("📖 Recent Proverbs Added")
if len(df) > 0:
    st.dataframe(df.tail(10).iloc[::-1], use_container_width=True)
else:
    st.info("No proverbs submitted yet. Be the first to add one!")
