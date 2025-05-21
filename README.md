# Spam-predictor-Web-using-Machine-Learning

A simple and intuitive web application that uses Machine Learning to detect spam messages. This project leverages Flask as the backend framework and implements a Bag of Words (CountVectorizer) model to convert text into numerical features. The trained model classifies whether an input message is Spam or Not Spam.

Features
 Input a message and get instant predictions.
 Machine Learning model trained on labeled SMS data.
 Preprocessing steps like lowercasing, punctuation removal, and stopword filtering.
 Uses Bag of Words (CountVectorizer) for feature extraction.
 Built with Flask for the backend and HTML/CSS for the frontend.

Tech Stack
Frontend: HTML, CSS and Java Script
Backend: Python, Flask
ML Model: Naive Bayes 
NLP Tools: CountVectorizer, NLTK 
Deployment:  live server

Project Structure

spam-predictor/
│
├── static/                  # CSS or JS files
├── templates/               # HTML templates
│   └── index.html
│
├── model/                   # Folder containing ML model and vectorizer
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── app.py                   # Main Flask application
├── preprocess.py            # Text preprocessing functions
├── requirements.txt         # Python dependencies
└── README.md                # This file

How It Works
Preprocessing: Input text is cleaned, lowercased, and tokenized.
Vectorization: The cleaned text is transformed using CountVectorizer.
Prediction: The vectorized text is passed to a trained ML model.
Output: The result is displayed as either Spam or Not Spam.

Installation
git clone https://github.com/jadonvansh2005/spam-predictor.git
cd spam-predictor

Install dependencies
pip install -r requirements.txt

Run the app
python app.py

Visit in your browser
http://127.0.0.1:5000/

