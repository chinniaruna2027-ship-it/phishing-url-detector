
import streamlit as st
import joblib

st.set_page_config(page_title="Phishing URL Detector", page_icon="🔐")

model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("🔐 Phishing URL Detector")
st.write("Check a URL using your trained Random Forest model.")

url = st.text_input("Enter a URL:")

if st.button("Check URL"):
    if url.strip():
        features = vectorizer.transform([url.strip()])
        prediction = str(model.predict(features)[0]).lower().strip()

        st.write("URL:", url)

        if prediction == "malicious":
            st.error("Prediction: Malicious URL ⚠️")
        elif prediction == "benign":
            st.success("Prediction: Benign URL ✅")
        else:
            st.warning(f"Model prediction: {prediction}")
    else:
        st.warning("Please enter a URL.")
