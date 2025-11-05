# import streamlit as st
# import pickle
# import re
# from nltk.corpus import stopwords

# stop_words = set(stopwords.words("english"))
# # load trained model + trained vectorizer
# model = pickle.load(open("model.pkl","rb"))
# tfidf = pickle.load(open("tfidf.pkl","rb"))

# def preprocess_text(text):
#     text = re.sub(r"[^a-zA-Z]", " ", text.lower())
#     tokens = [w for w in text.split() if w not in stop_words]
#     return " ".join(tokens)

# # ---------------- sidebar here ----------------
# st.sidebar.title("About Project")
# st.sidebar.write("""
# This Fake News Detector uses Machine Learning (LogisticRegression + TF-IDF)
# to classify news headlines as REAL or FAKE.
# """)

# st.sidebar.write("---")
# st.sidebar.write("Developed by: Sanchi")
# st.sidebar.write("Project Type: mini project")


# st.title("Fake news detection")

# input_text = st.text_area("Enter text")

# if st.button("Predict"):
#     clean = preprocess_text(input_text)
#     vect = tfidf.transform([clean])
#     pred = model.predict(vect)[0]

#     # >>> probability block INSIDE this IF <<<
#     proba = model.predict_proba(vect)[0]
#     fake_prob = proba[0] * 100     # index 0 → FAKE
#     real_prob = proba[1] * 100     # index 1 → REAL

#     st.write(f"Real Probability: {real_prob:.2f}%")
#     st.write(f"Fake Probability: {fake_prob:.2f}%")

    
















    
#     # if pred == 1:
#     #     st.success(f"REAL NEWS ✅ (Confidence {confidence:.2f}%)")
#     # else:
#     #     st.error(f"FAKE NEWS ❌ (Confidence {confidence:.2f}%)")


import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup

# Initialize stopwords
try:
    stop_words = set(stopwords.words("english"))
except:
    import nltk
    nltk.download('stopwords')
    stop_words = set(stopwords.words("english"))

# Load trained model + trained vectorizer
try:
    model = pickle.load(open("model.pkl", "rb"))
    tfidf = pickle.load(open("tfidf.pkl", "rb"))
except:
    st.error("Model files not found. Please ensure model.pkl and tfidf.pkl are in the same directory.")
    model = None
    tfidf = None

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text.lower())
    tokens = [w for w in text.split() if w not in stop_words]
    return " ".join(tokens)

def fetch_article_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract article text
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])
        
        return article_text if article_text else None
    except Exception as e:
        return None

# Custom CSS for Futuristic UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&display=swap');
    
    /* Main App Background */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #16213e 50%, #0a0e27 100%);
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border-right: 2px solid rgba(0, 240, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 240, 255, 0.2);
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #00f0ff;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 20px rgba(0, 240, 255, 0.8);
    }
    
    [data-testid="stSidebar"] p {
        color: #b8c5d6;
        font-size: 1rem;
    }
    
    /* Main Title */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #00f0ff, #ff006e, #00f0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(0, 240, 255, 0.5);
    }
    
    .subtitle {
        text-align: center;
        color: #8b97a8;
        font-size: 1.3rem;
        margin-bottom: 2rem;
    }
    
    /* Text Area Styling */
    .stTextArea textarea {
        background: rgba(10, 14, 39, 0.8) !important;
        border: 2px solid rgba(255, 0, 110, 0.3) !important;
        border-radius: 15px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 15px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #00f0ff !important;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.5) !important;
    }
    
    /* Text Input Styling */
    .stTextInput input {
        background: rgba(10, 14, 39, 0.8) !important;
        border: 2px solid rgba(0, 240, 255, 0.3) !important;
        border-radius: 15px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 15px !important;
    }
    
    .stTextInput input:focus {
        border-color: #ff006e !important;
        box-shadow: 0 0 20px rgba(255, 0, 110, 0.5) !important;
    }
    
    /* Button Styling */
    .stButton button {
        background: linear-gradient(90deg, #00f0ff, #ff006e) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 15px 50px !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        font-family: 'Orbitron', sans-serif !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 30px rgba(0, 240, 255, 0.4) !important;
    }
    
    .stButton button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 40px rgba(255, 0, 110, 0.6) !important;
    }
    
    /* Success/Error Box Styling */
    .stSuccess, .stError {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        border: 2px solid !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }
    
    .stSuccess {
        border-color: #39ff14 !important;
        color: #39ff14 !important;
        box-shadow: 0 0 30px rgba(57, 255, 20, 0.3) !important;
    }
    
    .stError {
        border-color: #ff006e !important;
        color: #ff006e !important;
        box-shadow: 0 0 30px rgba(255, 0, 110, 0.3) !important;
    }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        color: #00f0ff !important;
        font-family: 'Orbitron', sans-serif !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #39ff14, #00f0ff) !important;
        border-radius: 10px !important;
    }
    
    /* Divider */
    hr {
        border: 1px solid rgba(0, 240, 255, 0.3);
        margin: 2rem 0;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        color: #8b97a8;
        border-radius: 10px;
        padding: 10px 30px;
        font-weight: bold;
        font-size: 1.1rem;
        border: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #00f0ff, #ff006e) !important;
        color: white !important;
        border-color: #00f0ff !important;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("# 🛰 NEURAL DETECTOR")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 About Project")
st.sidebar.write("""
This Fake News Detector uses Machine Learning (Logistic Regression + TF-IDF) 
to classify news headlines as REAL or FAKE.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 Model Details")
st.sidebar.write("*Algorithm:* Logistic Regression")
st.sidebar.write("*Vectorizer:* TF-IDF")
st.sidebar.write("*Accuracy:* ~94.2%")

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Developed by:")
st.sidebar.markdown("*Mohit & Sanchi*")
st.sidebar.write("Project Type: Mini Project")

st.sidebar.markdown("---")
st.sidebar.info("⚡ Powered by Machine Learning")

# Main Content
st.markdown('<h1 class="main-title">🛰 FAKE NEWS DETECTOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by Machine Learning & TF-IDF Analysis</p>', unsafe_allow_html=True)

# Create tabs for input modes
tab1, tab2 = st.tabs(["📝 Text Input", "🔗 URL Input"])

input_text = ""

with tab1:
    st.markdown("### Enter News Headline or Article Text")
    input_text = st.text_area("", height=200, placeholder="🔍 Paste your news text here for AI analysis...", key="text_input")
    
    if st.button("⚡ ANALYZE TEXT", key="analyze_text"):
        if input_text.strip() and model and tfidf:
            with st.spinner("🔄 Analyzing..."):
                clean = preprocess_text(input_text)
                vect = tfidf.transform([clean])
                pred = model.predict(vect)[0]
                proba = model.predict_proba(vect)[0]
                
                fake_prob = proba[0] * 100
                real_prob = proba[1] * 100
                
                st.markdown("---")
                
                if pred == 1:
                    st.success(f"✅ REAL NEWS (Confidence: {real_prob:.2f}%)")
                else:
                    st.error(f"❌ FAKE NEWS (Confidence: {fake_prob:.2f}%)")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("🟢 Real Probability", f"{real_prob:.2f}%")
                with col2:
                    st.metric("🔴 Fake Probability", f"{fake_prob:.2f}%")
        elif not model or not tfidf:
            st.error("Model not loaded. Please check model files.")
        else:
            st.warning("Please enter some text to analyze.")

with tab2:
    st.markdown("### Enter Blog or News Article URL")
    url_input = st.text_input("", placeholder="🌐 https://example.com/news-article", key="url_input")
    
    if st.button("🌐 FETCH & ANALYZE", key="fetch_url"):
        if url_input.strip():
            with st.spinner("🔄 Fetching article content..."):
                article_content = fetch_article_content(url_input)
                
                if article_content and model and tfidf:
                    st.info(f"✅ Content fetched successfully! Analyzing...")
                    
                    clean = preprocess_text(article_content)
                    vect = tfidf.transform([clean])
                    pred = model.predict(vect)[0]
                    # proba = model.predict_proba(vect)[0]
                    
                    # fake_prob = proba[0] * 100
                    # real_prob = proba[1] * 100
                    
                    # st.markdown("---")
                    
                    # if pred == 1:
                    #     st.success(f"✅ REAL NEWS (Confidence: {real_prob:.2f}%)")
                    # else:
                    #     st.error(f"❌ FAKE NEWS (Confidence: {fake_prob:.2f}%)")
                    proba = model.predict_proba(vect)[0]

                    real_prob = proba[1] * 100
                    fake_prob = proba[0] * 100

                    if pred == 1:
                        st.success(f"✅ REAL NEWS (Confidence: {real_prob:.2f}%)")
                    else:
                        st.error(f"❌ FAKE NEWS (Confidence: {fake_prob:.2f}%)")


                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("🟢 Real Probability", f"{real_prob:.2f}%")
                    with col2:
                        st.metric("🔴 Fake Probability", f"{fake_prob:.2f}%")
                    
                    with st.expander("📄 View Extracted Content"):
                        st.write(article_content[:500] + "..." if len(article_content) > 500 else article_content)
                elif not model or not tfidf:
                    st.error("Model not loaded. Please check model files.")
                else:
                    st.error("❌ Failed to fetch article content. Please check the URL and try again.")
        else:
            st.warning("Please enter a valid URL.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #8b97a8;'>Powered by Streamlit ⚡ | ML Model: Logistic Regression</p>", unsafe_allow_html=True)