📧 MailGuard AI – Email Spam Detection


🛡️ An intelligent spam email classifier built with Machine Learning and Streamlit

🚀 Features
    .🧠 ML Model: Trained using Naive Bayes classifier on a TF-IDF feature vector.
    .📥 User Input: Paste email content or upload a .txt file.
    .⚙️ Instant Predictions: Detect whether an email is SPAM or NOT SPAM.
    .📊 Model Dashboard: View Accuracy, Precision, Recall, and F1-Score.
    .📁 Prediction History: View past predictions within the session.


🖼️ Interface Preview
<img src="https://private-user-images.githubusercontent.com/157392765/462928950-fb309a49-75ed-459b-a880-cbd768156aeb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE4MTM3MzMsIm5iZiI6MTc1MTgxMzQzMywicGF0aCI6Ii8xNTczOTI3NjUvNDYyOTI4OTUwLWZiMzA5YTQ5LTc1ZWQtNDU5Yi1hODgwLWNiZDc2ODE1NmFlYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNlQxNDUwMzNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01YmYzMzQ4MzFkNWQ0NWI1NmI2OTI5MTExNGZhYTEwZGYyZGQ4ZTZiZTcwZDA4ZDg5OGE1NmJmM2QwMmE5ZTEwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Bc8PCdmDP4Kf0opuFxaRE1N3MAnNH2E564gpM0YeCJg" alt="App Screenshot" width="800"/>

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


