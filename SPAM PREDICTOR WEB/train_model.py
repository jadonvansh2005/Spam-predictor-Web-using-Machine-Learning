import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example training data
texts = ["Free money now!!!", "Hi, how are you?", "Win a lottery", "Let's meet for coffee"]
labels = [1, 0, 1, 0]  # 1 = spam, 0 = ham

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save model
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)


import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Training data
texts = ["Free money!!!", "Hi, how are you?", "Win cash now", "Let's catch up tomorrow"]
labels = [1, 0, 1, 0]  # 1 = spam, 0 = ham

# Step 2: Create and fit vectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Step 3: Train the model
model = MultinomialNB()
model.fit(X, labels)

# Step 4: Save model and vectorizer
joblib.dump(model, 'spam_model.pkl')         # Correct name for Flask app
joblib.dump(vectorizer, 'vectorizer.pkl')
