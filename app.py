import streamlit as st
import pickle
import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

# load trained model + trained vectorizer
model = pickle.load(open("model.pkl","rb"))
tfidf = pickle.load(open("tfidf.pkl","rb"))

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text.lower())
    tokens = [w for w in text.split() if w not in stop_words]
    return " ".join(tokens)

# ---------------- sidebar here ----------------
st.sidebar.title("About Project")
st.sidebar.write("""
This Fake News Detector uses Machine Learning (LogisticRegression + TF-IDF)
to classify news headlines as REAL or FAKE.
""")

st.sidebar.write("---")
st.sidebar.write("Developed by: Sanchi")
st.sidebar.write("Project Type: mini project")


st.title("Fake news detection")

input_text = st.text_area("Enter text")

if st.button("Predict"):
    clean = preprocess_text(input_text)
    vect = tfidf.transform([clean])
    pred = model.predict(vect)[0]

    # >>> probability block INSIDE this IF <<<
    proba = model.predict_proba(vect)[0]
    fake_prob = proba[0] * 100     # index 0 → FAKE
    real_prob = proba[1] * 100     # index 1 → REAL

    st.write(f"Real Probability: {real_prob:.2f}%")
    st.write(f"Fake Probability: {fake_prob:.2f}%")

    
    # if pred == 1:
    #     st.success(f"REAL NEWS ✅ (Confidence {confidence:.2f}%)")
    # else:
    #     st.error(f"FAKE NEWS ❌ (Confidence {confidence:.2f}%)")


