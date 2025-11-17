import streamlit as st
import pandas as pd
import google.generativeai as genai

genai.configure(api_key=("AIzaSyDqferTB7u2X44NuEPEQKgO2tYIVfmV0fE"))

df = pd.read_excel("MTA_Daily_Ridership.csv")
def ask_gemini(question, df):
    context = df.head(100).to_string(index=False)
    prompt = f"""
    You are a data analysis assistant. 
    The user is asking a question about a sample dataset.
    {context}
    
    Based on this data, answer the question clearly:
    {question}
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Kaggle Survey Analysis Chatbot", page_icon="📊", layout="wide")

# ====== تصميم احترافي كامل باللون الأزرق ======
st.markdown(
    """
    <style>
        /* الخلفية الرئيسية للصفحة */
        .stApp {
            background: linear-gradient(to bottom, #1CABE2, #ffffff);
            color: #000000;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Sidebar مظلل */
        .css-1d391kg {
            background-color: #007ACC;
            padding: 20px;
            border-radius: 10px;
        }

        /* العناوين */
        h1 {
            color: #ffffff;
            text-shadow: 1px 1px 2px #000000;
        }
        h2, h3, h4, p {
            color: #000000;
        }

        /* Text area */
        .stTextArea textarea {
            background-color: #f0f8ff;
            border: 1px solid #b0b0b0;
            border-radius: 10px;
            padding: 10px;
        }

        /* Buttons */
        .stButton button {
            background-color: #005f99;
            color: white;
            border-radius: 10px;
            padding: 10px 25px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #004f80;
            cursor: pointer;
        }

        /* Cards للإجابة */
        .answer-card {
            background-color: #ffffffcc;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.3);
        }

        /* صورة في مكان السؤال */
        .main-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 250px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        }
    </style>

    <div style="text-align:center; margin-bottom:30px;">
        <img class="main-image" src="https://th.bing.com/th/id/OIP.Ii0ROnrWLvyuSHP3wzjhZwHaE8?pid=ImgDetMain" alt="Logo">
        <h1>Kaggle Survey Analysis Chatbot</h1>
        <p style="font-size:18px;">Ask questions about your dataset or pick one from the sidebar</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ====== Sidebar ======
st.sidebar.header("📌 Pinned Questions")
Pinned_questions = [
    "What is the most common programming language used by data professionals?",
    "What is the average salary of data scientists?",
    "What is the most popular machine learning framework?",
    "What education level do most participants have?",
    "Which country has the highest number of survey respondents?"
]
selected_question = st.sidebar.radio("Select a question:", options=[""] + Pinned_questions, index=0)

# ====== Main Content ======
st.subheader("✍️ Write your question:")
user_question = st.text_area("Input your question here...", height=120)

final_question = selected_question if selected_question.strip() else user_question if user_question.strip() else None

if final_question:
    with st.spinner("⏳ Gemini is thinking..."):
        answer = ask_gemini(final_question, df)
    
    st.markdown(f"""
    <div class="answer-card">
        <h3>✅ Answer:</h3>
        <p>{answer}</p>
    </div>
    """, unsafe_allow_html=True)















