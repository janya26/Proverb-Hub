import streamlit as st

# Store proverbs in session state (memory only)
if "proverbs" not in st.session_state:
    st.session_state.proverbs = []

# App title
st.set_page_config(page_title="ProverbHub - Telugu Edition")
st.title("🪔 ProverbHub - తెలుగు నానుడి కేంద్రం")

st.markdown("మీకు తెలిసిన తెలుగునానుడిని మరియు దాని అర్థాన్ని నమోదు చేయండి👇")

# Input form
with st.form(key="proverb_form"):
    telugu = st.text_input("నానుడి (Telugu Proverb)")
    meaning = st.text_area("అర్థం (Meaning in Telugu)")
    submit = st.form_submit_button("సమర్పించండి")

if submit:
    if telugu.strip() and meaning.strip():
        st.session_state.proverbs.append((telugu.strip(), meaning.strip()))
        st.success("✅ నానుడి విజయవంతంగా జోడించబడింది!")
    else:
        st.warning("⚠️ దయచేసి నానుడి మరియు అర్థం రెండింటినీ నమోదు చేయండి.")

# Display section
if st.session_state.proverbs:
    st.subheader("📝 సమర్పించిన నానుడులు")
    for i, (prov, mean) in enumerate(st.session_state.proverbs[::-1], 1):
        st.markdown(f"**{i}. {prov}**  \n📖 {mean}")
else:
    st.info("ఇంకా ఏ నానుడి జోడించబడలేదు. మీరు మొదటివారిగా ఉండవచ్చు!")
