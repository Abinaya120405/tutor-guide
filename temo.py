import streamlit as st

st.title("🕵️ Fake Job Posting Detector")

user_input = st.text_area("Enter Job Description")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        # TEMPORARY DEMO RESULT
        st.success("✅ This looks like a REAL job posting")
        # or
        # st.error("🚨 This looks like a FAKE job posting")