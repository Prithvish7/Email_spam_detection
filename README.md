📧 MailGuard AI – Email Spam Detection


🛡️ An intelligent spam email classifier built with Machine Learning and Streamlit

🚀 Features
    .🧠 ML Model: Trained using Naive Bayes classifier on a TF-IDF feature vector.
    .📥 User Input: Paste email content or upload a .txt file.
    .⚙️ Instant Predictions: Detect whether an email is SPAM or NOT SPAM.
    .📊 Model Dashboard: View Accuracy, Precision, Recall, and F1-Score.
    .📁 Prediction History: View past predictions within the session.


🖼️ Interface Preview
<img src="https://github.com/anirbanmahato616/Email_spam_detection/issues/1" alt="App Screenshot" width="800"/>

🧠 How It Works
    1.Input email via text box or .txt file.
    2.The app vectorizes the text using a TF-IDF vectorizer.
    3.The trained Naive Bayes model predicts if it’s SPAM or NOT SPAM.
    4.Displays prediction 
    5.Tracks recent predictions in session history.

🛠️ Tech Stack
    .Python 3.12
    .Scikit-learn (for model & vectorization)
    .Streamlit (for frontend)
    .Seaborn, Plotly (for visualization)

📦 Installation
    1.Clone the repository:-
    
        git clone https://github.com/your-username/Email-Spam-Detection.git
        
        cd Email-Spam-Detection

    2.Install dependencies:-
        pip install -r requirements.txt

    3.Run the app:-
        streamlit run app.py

📈 Model Performance:-
    Metric	    Score
    Accuracy	96.80%
    Precision	97.10%
    Recall	    97.10%
    F1-Score	97.10%

🗂 Dataset
    https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset?select=combined_data.csv


