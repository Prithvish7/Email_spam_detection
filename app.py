import streamlit as st
import pickle

# Load the saved model
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the saved TF-IDF vectorizer
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Set up Streamlit app
st.set_page_config(page_title="Email Spam Detector", page_icon="📧")
st.title("🛡️Email Spam Detector🛡️")

st.markdown("### Paste an email below to check if it's Spam or Not Spam")

# User input
email_input = st.text_area("Email Content:", height=200)

# Predict button
if st.button("Predict"):
    if email_input.strip() == "":
        st.warning("Please enter some email text.")
    else:
        # Transform the input using the loaded vectorizer
        features = vectorizer.transform([email_input])

        # Predict using the model
        prediction = model.predict(features)[0]

        # Display result
        if prediction == 1:
            st.error("🫷 This email is **SPAM**!")
        else:
            st.success("🤘This email is **NOT SPAM**.")
# Footer
st.markdown("""<hr style="margin-top: 50px;">""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 14px; color: gray;'>
🚀 Built with ❤️ by Prithvish, Anirban & Sayantan | Powered by Streamlit & ML
</p>
""", unsafe_allow_html=True)

# ✅ resolved version
print("This is the correct final version")
