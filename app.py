import streamlit as st
import pandas as pd
import os

# File path in current directory
CSV_FILE = "proverbs.csv"

# Load or create the DataFrame
def load_proverbs():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["Proverb", "Meaning"])

# Save new proverb to the CSV
def save_proverb(proverb, meaning):
    try:
        df = load_proverbs()
        new_row = {"Proverb": proverb, "Meaning": meaning}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        return True
    except Exception as e:
        st.warning(f"⚠️ Proverb added, but couldn't save to CSV.\n\n{e}")
        return False

# Streamlit UI
st.title("📜 తెలుగు నానుడి గూడు")
st.subheader("Add a Telugu proverb and its meaning")

# User input
telugu = st.text_input("నానుడి (Proverb in Telugu)")
meaning = st.text_area("అర్థం (Meaning in Telugu)")

if st.button("Add Proverb"):
    if telugu.strip() == "" or meaning.strip() == "":
        st.warning("Both fields are required!")
    else:
        success = save_proverb(telugu.strip(), meaning.strip())
        if success:
            st.success("✅ Proverb added successfully!")

# Show current proverbs
with st.expander("📖 View Saved Proverbs"):
    df = load_proverbs()
    if df.empty:
        st.info("No proverbs added yet.")
    else:
        st.dataframe(df)
