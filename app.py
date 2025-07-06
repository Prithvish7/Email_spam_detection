import streamlit as st
import pickle
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# Load model and vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown("""
    <div style='display: flex; align-items: center; margin-bottom: 0px;'>
    <h1 style="
        font-family: 'Poppins', sans-serif;
        font-size: 40px;
        background: linear-gradient(to right, #ff512f, #dd2476);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-right: 20px;
    ">
        MailGuard AI
    </h1>
</div>
""", unsafe_allow_html=True)

# Navigation Bar using option_menu
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "How it Works", "Performance", "Contact"],
    icons=["house", "info-circle", "gear", "bar-chart", "envelope"],
    menu_icon="cast",
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#bd2f0c"},
        "icon": {"color": "black", "font-size": "16px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#2D1163", "color": "white"},
    }
)

# History session
if "history" not in st.session_state:
    st.session_state.history = []

if selected == "Home":
    #st.title("MailGuard AI 📧")
    st.markdown("""
        ### Paste an email below or upload a file to check if it's **Spam** or **Not Spam**
    """)

    email_input = st.text_area("📥 Email Content:", height=200, placeholder="Paste your email content here...")
    uploaded_file = st.file_uploader("Or upload an email text file (.txt)", type=["txt"])

    if uploaded_file is not None:
        email_input = uploaded_file.read().decode("utf-8")
        st.text_area("Uploaded Email Content:", value=email_input, height=200)

    predict_clicked = st.button("🚀 Predict", use_container_width=True)
    
    if predict_clicked:
        if not email_input.strip():
            st.warning("Please enter or upload some email text.")
        else:
            features = vectorizer.transform([email_input])
            prediction = model.predict(features)[0]
            prediction_proba = model.predict_proba(features)[0][1]

            st.session_state.history.append({
                "email": email_input[:100] + ("..." if len(email_input) > 100 else ""),
                "prediction": "SPAM" if prediction == 1 else "NOT SPAM"
            })

            if prediction == 1:
                st.error(f"🚫 SPAM MAIL!")
            else:
                st.success(f"📩 NOT SPAM.")

    if st.session_state.history:
        st.markdown("---")
        st.markdown("### 🕘 Prediction History")
        for i, record in enumerate(reversed(st.session_state.history), 1):
            st.markdown(
                f"**{i}.** {record['email']}  \\n                Prediction: **{record['prediction']}**"
            )

elif selected == "About":
    st.header("📌 About the Project")
    st.write("""
**MailGuard AI** is a smart, machine learning-powered web app designed to detect spam emails with high accuracy.  
It uses a trained **Naive Bayes classifier** along with **TF-IDF vectorization** to understand email content.

With an easy-to-use interface and clean visuals, MailGuard AI makes spam detection fast, interactive, and effortless — whether you're pasting a message or uploading a file.

🧠 Built with Machine Learning  
📊 Powered by real-time predictions  
🎯 Designed for simplicity and precision
""")


elif selected == "How it Works":
    st.header("⚙️ How It Works")
    st.markdown("""
-  **Paste** your email content or 📄 **upload** a .txt file.
-  Hit the **Predict** button to start the magic.
-  Our AI scans the message instantly and tells you if it’s **SPAM** or **NOT SPAM**.
-  Check your **prediction history** below anytime.
""")


elif selected == "Performance":
    st.subheader("📈 Model Performance Dashboard")
    metrics = {
        "Accuracy": 96.80,
        "Precision": 97.10,
        "Recall": 97.10,
        "F1-Score": 97.10
    }

    def gauge_chart(title, value, max_value=100):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title},
            gauge={
                'axis': {'range': [0, max_value]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, max_value * 0.5], 'color': "#d3d3d3"},
                    {'range': [max_value * 0.5, max_value], 'color': "#a9a9a9"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': value
                }
            }
        ))
        fig.update_layout(height=250, margin=dict(l=10, r=10, t=30, b=10))
        return fig

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.plotly_chart(gauge_chart("Accuracy", metrics["Accuracy"]), use_container_width=True)
    with col2:
        st.plotly_chart(gauge_chart("Precision", metrics["Precision"]), use_container_width=True)
    with col3:
        st.plotly_chart(gauge_chart("Recall", metrics["Recall"]), use_container_width=True)
    with col4:
        st.plotly_chart(gauge_chart("F1-Score", metrics["F1-Score"]), use_container_width=True)

elif selected == "Contact":
    st.header("📬 Contact Us")
    st.write("""
    **MailGuard.AI**  
    📧 mailguardai@gmail.com  
    📱 +91-1234567890
    """)

# Footer
st.markdown(
    """
    <hr style="margin-top: 50px;">
    <p style='text-align: center; font-size: 14px; color: gray;'>
Developed by Team <strong>MailGuard AI</strong><br>
 Last Updated: July 2025
</p>

    """,
    unsafe_allow_html=True,
)
