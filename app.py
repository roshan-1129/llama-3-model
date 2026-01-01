import os
from dotenv import load_dotenv

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

#page
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# css
st.markdown("""
<style>
/* Entire app background */
.stApp {
    background-color: #0f0f0f;
    color: #ffffff;
}

/* Title */
h1 {
    text-align: center;
    color: #00e5ff;
    font-weight: 700;
}

/* Input box */
.stTextInput > div > div > input {
    background-color: #1a1a1a;
    color: white;
    border-radius: 8px;
    border: 1px solid #333;
}

/* User message */
.user-msg {
    background-color: #1f2937;
    padding: 12px 16px;
    border-radius: 10px;
    margin: 10px 0;
    text-align: right;
}

/* Bot message */
.bot-msg {
    background-color: #111827;
    padding: 12px 16px;
    border-radius: 10px;
    margin: 10px 0;
    text-align: left;
    border-left: 4px solid #00e5ff;
}

/* Footer */
.footer {
    text-align: center;
    color: #777;
    font-size: 13px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


st.title("🤖 LangChain Chatbot (LLaMA 3)")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful, professional AI assistant."),
        ("user", "Question: {question}")
    ]
)

#llm model
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


input_text = st.text_input("💬 Ask something...", placeholder="Type your question here...")

if input_text:
    response = chain.invoke({"question": input_text})

    st.session_state.chat_history.append(("user", input_text))
    st.session_state.chat_history.append(("bot", response))


for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"<div class='user-msg'>🧑 {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>🤖 {message}</div>", unsafe_allow_html=True)


st.markdown(
    "<div class='footer'>Powered by LangChain • Ollama • LLaMA 3</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='footer'>Developed by ROSHAN S</div>",
    unsafe_allow_html=True
)


