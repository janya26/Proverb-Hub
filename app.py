import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Telugu ProverbHub", layout="centered")

# Path to save CSV file in Hugging Face
data_file = "/data/proverbs.csv"

# Title
st.title("🌾 Telugu ProverbHub")
st.markdown("Share and explore traditional Telugu proverbs! 🇮🇳🪔")

# --- Form to Add New Proverb ---
st.header("📌 Add a Telugu Proverb")
with st.form(key="add_proverb"):
    telugu = st.text_area("✍️ Telugu Proverb", placeholder="Example: తినే తిండి లేకుంటే తల పట్టుకోవడం ఎలాగో", max_chars=200)
    meaning = st.text_area("💬 Meaning / Usage", placeholder="Use this space to explain what it means or when it’s used", max_chars=300)
    submit = st.form_submit_button("Add Proverb")

# --- Save to CSV ---
def save_proverb(telugu, meaning):
    os.makedirs("/data", exist_ok=True)  # Create folder if not there
    df = pd.DataFrame([[telugu, meaning]], columns=["Telugu Proverb", "Meaning/Usage"])
    try:
        if os.path.exists(data_file):
            df.to_csv(data_file, mode='a', header=False, index=False)
        else:
            df.to_csv(data_file, mode='w', header=True, index=False)
        return True
    except Exception as e:
        st.warning(f"⚠️ Proverb added, but couldn't save to CSV (read-only system).\n\n{e}")
        return False

if submit:
    if telugu and meaning:
        success = save_proverb(telugu.strip(), meaning.strip())
        if success:
            st.success("✅ Proverb saved successfully!")
    else:
        st.error("🚨 Both fields are required.")

# --- Show Saved Proverbs ---
st.header("📚 Explore Added Proverbs")
if os.path.exists(data_file):
    try:
        data = pd.read_csv(data_file)
        if not data.empty:
            st.dataframe(data, use_container_width=True)
        else:
            st.info("No proverbs added yet. Be the first! 🌱")
    except Exception as e:
        st.error(f"Could not load proverbs: {e}")
else:
    st.info("No proverbs saved yet. 🚀 Add your first one above!")
