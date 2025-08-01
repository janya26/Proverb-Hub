import streamlit as st
import pandas as pd
import os

# CSV file path in Hugging Face writable directory
data_file = "/data/proverbs.csv"

# Load existing proverbs or create empty DataFrame
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    df = pd.DataFrame(columns=["Proverb", "Meaning / Usage"])

st.set_page_config(page_title="ProverbHub – Telugu Proverbs", layout="centered")
st.title("📜 ProverbHub – Telugu Proverbs")

st.markdown("Contribute your favorite Telugu proverbs and their meanings to preserve our culture 🌾✨")

with st.form("proverb_form"):
    proverb = st.text_input("Enter the **Telugu Proverb**:")
    meaning = st.text_area("Enter its **Meaning or Usage** (in Telugu or English):")

    submitted = st.form_submit_button("Submit Proverb")

    if submitted:
        if proverb.strip() and meaning.strip():
            new_entry = {"Proverb": proverb.strip(), "Meaning / Usage": meaning.strip()}
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

            # Try saving to /data
            try:
                df.to_csv(data_file, index=False)
                st.success("✅ Proverb added and saved successfully!")
            except Exception as e:
                st.warning("⚠️ Proverb added, but couldn't save to CSV (read-only system).")
                st.error(f"{e}")
        else:
            st.error("🚫 Please fill out both fields.")

# Show existing proverbs
if not df.empty:
    st.markdown("---")
    st.subheader("📚 Proverbs Collection")
    st.dataframe(df[::-1], use_container_width=True)
else:
    st.info("No proverbs added yet. Be the first to contribute! 🌱")

