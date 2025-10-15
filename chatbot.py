import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

genai.configure(api_key=("AIzaSyDqferTB7u2X44NuEPEQKgO2tYIVfmV0fE"))

df = pd.read_excel(r"C:\Users\AL HASSAN\Downloads\kaggle_survey_2020_responses\cleaned_kaggle_dashboard10.xlsx")

def ask_gemini(question, df):

    context = df.head(100).to_string(index=False)
    
    prompt = f"""
    You are a data analysis assistant. 
    The user is asking a question about a large dataset.
    {context}
    
    Based on this data, answer the question clearly:
    {question}
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Kaggle Survey analysis Chatbot", page_icon="📋", layout="wide")
st.markdown(
    """
    <div style="text-align:center;">
        <img src="https://th.bing.com/th/id/OIP.Ii0ROnrWLvyuSHP3wzjhZwHaE8?pid=ImgDetMain" 
             alt="Logo" width="300" style="border-radius:15px;margin-bottom:15px;">
        <h1 style="color:#1CABE2;">Kaggle Survey Analysis Chatbot</h1>
        <p style="color:white;font-size:18px;margin-top:-5px;">
        Ask questions about your data directly or choose one from the sidebar.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("📌 Pinned Questions")
Pinned_questions = [
    "What is the most common programming language used by data professionals?",
    "What is the average salary of data scientists?",
    "What is the most popular machine learning framework?",
    "What education level do most participants have?",
    "Which country has the highest number of survey respondents?"
]

selected_question = st.sidebar.radio("Select a question:", options=[""] + Pinned_questions, index=0)
st.subheader("✍️ Write your question:")
user_question = st.text_area("Input your question here...", height=120)


final_question = None
if selected_question and selected_question.strip():
    final_question = selected_question
elif user_question.strip():
    final_question = user_question

if final_question:
    with st.spinner("⏳ Gemini is thinking..."):
        answer = ask_gemini(final_question, df)
    st.write("✅ Answer:")
    st.write(answer)
