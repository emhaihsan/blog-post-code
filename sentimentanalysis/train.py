import pandas as pd
import re
import nltk
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# Load the dataset
data = pd.read_csv('data/sentiment140.csv', encoding='latin-1', header=None)
data.columns = ['target', 'ids', 'date', 'flag', 'user', 'text']

# Drop unnecessary columns
data = data.drop(columns=['ids', 'date', 'flag', 'user'])

# Convert target to binary (0: Negative, 1: Positive)
data['target'] = data['target'].apply(lambda x: 1 if x == 4 else 0)

# Create a balanced subset of 5% of the data
positive_samples = data[data['target'] == 1].sample(frac=0.05, random_state=42)
negative_samples = data[data['target'] == 0].sample(frac=0.05, random_state=42)
five_percent_data = pd.concat([positive_samples, negative_samples])

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

five_percent_data['text'] = five_percent_data['text'].apply(preprocess_text)

# Split the dataset and vectorize text data
X = five_percent_data['text']
y = five_percent_data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=5000)
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Save the vectorizer
joblib.dump(vectorizer, 'model/tfidf_vectorizer.pkl')

# Train and save Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train_vect, y_train)
joblib.dump(nb_model, 'model/naive_bayes_model.pkl')

# Train and save SVM model
svm_model = SVC()
svm_model.fit(X_train_vect, y_train)
joblib.dump(svm_model, 'model/svm_model.pkl')

# Train and save Logistic Regression model
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_vect, y_train)
joblib.dump(lr_model, 'model/logistic_regression_model.pkl')

# Evaluate models
y_pred_nb = nb_model.predict(X_test_vect)
y_pred_svm = svm_model.predict(X_test_vect)
y_pred_lr = lr_model.predict(X_test_vect)

print("Naive Bayes Model")
print("Accuracy:", accuracy_score(y_test, y_pred_nb))
print("Classification Report:\n", classification_report(y_test, y_pred_nb))

print("SVM Model")
print("Accuracy:", accuracy_score(y_test, y_pred_svm))
print("Classification Report:\n", classification_report(y_test, y_pred_svm))

print("Logistic Regression Model")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Classification Report:\n", classification_report(y_test, y_pred_lr))

# # Compare model performances using a bar chart (optional)
# models = ['Naive Bayes', 'SVM', 'Logistic Regression']
# accuracies = [accuracy_score(y_test, y_pred_nb), accuracy_score(y_test, y_pred_svm), accuracy_score(y_test, y_pred_lr)]

# plt.figure(figsize=(10, 5))
# sns.barplot(x=models, y=accuracies)
# plt.title('Comparison of Model Accuracies')
# plt.ylabel('Accuracy')
# plt.show()
