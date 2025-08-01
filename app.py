import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="TeluguVillageBot – Proverbs Collector", layout="centered")

st.title("🌾 TeluguVillageBot: Add a Telugu Proverb")

# CSV file path (must match persistent storage mount)
data_file = "proverbs.csv"

# Ensure the file exists and has the correct header
if not os.path.exists(data_file):
    try:
        with open(data_file, "w", encoding="utf-8") as f:
            f.write("Proverb,Meaning/Usage\n")
    except Exception as e:
        st.warning("⚠️ Could not create CSV file: " + str(e))

# Input fields
with st.form("proverb_form"):
    proverb = st.text_input("📝 Enter a Telugu Proverb")
    meaning = st.text_area("💬 Meaning or Usage of the Proverb")
    submitted = st.form_submit_button("✅ Submit")

    if submitted:
        if not proverb.strip():
            st.error("Please enter a valid proverb.")
        elif not meaning.strip():
            st.error("Please provide a meaning or usage.")
        else:
            # Try appending to the CSV
            try:
                df = pd.DataFrame([[proverb, meaning]], columns=["Proverb", "Meaning/Usage"])
                df.to_csv(data_file, mode="a", index=False, header=False, encoding="utf-8")
                st.success("✅ Proverb added successfully!")
            except Exception as e:
                st.warning("⚠️ Proverb added, but couldn't save to CSV (read-only system).\n\n" + str(e))

# Optional: View the current data (toggle)
with st.expander("📜 View Submitted Proverbs"):
    try:
        df = pd.read_csv(data_file)
        st.dataframe(df)
    except:
        st.info("No data to show yet or unable to read CSV.")
