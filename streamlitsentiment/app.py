import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords from NLTK
nltk.download('stopwords')

# Function for text preprocessing
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    text = text.split()  # Split into words
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]  # Remove stopwords and perform stemming
    text = ' '.join(text)
    return text

# Load the vectorizer and models
vectorizer = joblib.load('./model/tfidf_vectorizer.pkl')
svm_model = joblib.load('./model/svm_model.pkl')
nb_model = joblib.load('./model/naive_bayes_model.pkl')
lr_model = joblib.load('./model/logistic_regression_model.pkl')

# App title
st.title("Tweet Sentiment Analysis App")
st.write("Enter the text you want to analyze for sentiment:")

# User input text
input_text = st.text_area("Input text here")

# Model selection
st.write("Select models for sentiment analysis:")
use_nb = st.checkbox('Naive Bayes')
use_svm = st.checkbox('SVM')
use_lr = st.checkbox('Logistic Regression')

if st.button("Analyze"):
    if not input_text:
        st.write("Please enter the text for analysis.")
    elif not (use_nb or use_svm or use_lr):
        st.write("Please select at least one model for analysis.")
    else:
        # Process the input text
        input_text_processed = preprocess_text(input_text)
        input_text_vect = vectorizer.transform([input_text_processed])

        st.write(f"**Input Text:** {input_text}")
        
        # Prediction using Naive Bayes
        if use_nb:
            nb_prediction = nb_model.predict(input_text_vect)[0]
            nb_prob = nb_model.predict_proba(input_text_vect)[0]
            st.write(f"**Naive Bayes Prediction:** {'Positive' if nb_prediction == 1 else 'Negative'} (Confidence: {nb_prob[nb_prediction]:.2f})")

        # Prediction using SVM
        if use_svm:
            svm_prediction = svm_model.predict(input_text_vect)[0]
            st.write(f"**SVM Prediction:** {'Positive' if svm_prediction == 1 else 'Negative'}")

        # Prediction using Logistic Regression
        if use_lr:
            lr_prediction = lr_model.predict(input_text_vect)[0]
            lr_prob = lr_model.predict_proba(input_text_vect)[0]
            st.write(f"**Logistic Regression Prediction:** {'Positive' if lr_prediction == 1 else 'Negative'} (Confidence: {lr_prob[lr_prediction]:.2f})")

