import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# Preprocess text data
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    text = text.split()  # Split into words
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]  # Remove stopwords and stem words
    text = ' '.join(text)
    return text

# Load the vectorizer and models
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')
nb_model = joblib.load('model/naive_bayes_model.pkl')
svm_model = joblib.load('model/svm_model.pkl')
lr_model = joblib.load('model/logistic_regression_model.pkl')

# Example usage with new text data
new_text = ["I love this product!", "This is the worst service ever."]
new_text_processed = [preprocess_text(text) for text in new_text]
new_text_vect = vectorizer.transform(new_text_processed)

# Predict using Naive Bayes
nb_predictions = nb_model.predict(new_text_vect)
print("Naive Bayes Predictions:", nb_predictions)

# Predict using SVM
svm_predictions = svm_model.predict(new_text_vect)
print("SVM Predictions:", svm_predictions)

# Predict using Logistic Regression
lr_predictions = lr_model.predict(new_text_vect)
print("Logistic Regression Predictions:", lr_predictions)
