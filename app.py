import streamlit as st
import pandas as pd
import os

# Path to your CSV file (should already exist with headers)
data_file = "proverbs.csv"

# Load existing data or create empty DataFrame if something breaks
try:
    df = pd.read_csv(data_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Proverb", "Meaning", "Language"])

st.title("🌱 ProverbHub - Add a Proverb")

# User input fields
proverb = st.text_input("Enter a Proverb")
meaning = st.text_area("What does it mean?")
language = st.selectbox("Language", ["Telugu", "Hindi", "Tamil", "Malayalam", "Kannada", "Other"])

if st.button("Submit"):
    if proverb and meaning:
        # Create a new entry
        new_entry = {"Proverb": proverb, "Meaning": meaning, "Language": language}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

        # Try saving to the CSV (may fail in read-only Docker environments)
        try:
            df.to_csv(data_file, index=False)
            st.success("✅ Proverb added successfully!")
        except PermissionError:
            st.warning("⚠️ Proverb added, but couldn't save to CSV (read-only file system).")

        # Show current table
        st.subheader("📜 All Proverbs So Far")
        st.dataframe(df)

    else:
        st.error("Please enter both the proverb and its meaning.")

