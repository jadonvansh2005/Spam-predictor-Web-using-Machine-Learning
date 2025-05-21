from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def check_spam(message):
    data = [message]
    vect = vectorizer.transform(data)
    prediction = model.predict(vect)
    return "🚨 Spam Detected!" if prediction[0] == 1 else "✅ Not Spam!"


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""  
    message = ""
    
    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            result = check_spam(message)
    
    return render_template("index.html", result=result, message=message)

if __name__ == "__main__":
    app.run(debug=True)

