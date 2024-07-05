import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import argparse

nltk.download('stopwords')

# Preprocess text data
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Menghapus URL
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Menghapus tanda baca
    text = text.lower()  # Mengonversi ke huruf kecil
    text = text.split()  # Membagi teks menjadi kata-kata
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]  # Menghapus stopwords dan melakukan stemming
    text = ' '.join(text)
    return text

# Memuat vektorizer dan model
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')
nb_model = joblib.load('model/naive_bayes_model.pkl')
svm_model = joblib.load('model/svm_model.pkl')
lr_model = joblib.load('model/logistic_regression_model.pkl')

# Argument parser
parser = argparse.ArgumentParser(description='Predict sentiment of input text.')
parser.add_argument('-t','--text', type=str, help='Text to analyze sentiment')
args = parser.parse_args()

# Memproses teks input
input_text = args.text
input_text_processed = preprocess_text(input_text)
input_text_vect = vectorizer.transform([input_text_processed])

# Prediksi menggunakan Naive Bayes
nb_prediction = nb_model.predict(input_text_vect)[0]
nb_prob = nb_model.predict_proba(input_text_vect)[0]

# Prediksi menggunakan SVM
svm_prediction = svm_model.predict(input_text_vect)[0]

# Prediksi menggunakan Logistic Regression
lr_prediction = lr_model.predict(input_text_vect)[0]
lr_prob = lr_model.predict_proba(input_text_vect)[0]

# Menampilkan prediksi
print(f"Input text: {input_text}")
print(f"Naive Bayes: {'Positive' if nb_prediction == 1 else 'Negative'} (Confidence: {nb_prob[nb_prediction]:.2f})")
print(f"SVM: {'Positive' if svm_prediction == 1 else 'Negative'}")
print(f"Logistic Regression: {'Positive' if lr_prediction == 1 else 'Negative'} (Confidence: {lr_prob[lr_prediction]:.2f})")
