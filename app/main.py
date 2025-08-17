import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables and configure page
load_dotenv()
st.set_page_config(
    page_title="DMR Chat Interface",
    page_icon="🤖",
    layout="wide"
)

# Initialize OpenAI client
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Application Header
st.title("🤖 Chat with LLM from Docker Model Runner")
st.markdown("---")

# Chat interface
if st.session_state.messages:
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate and display response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=os.getenv("MODEL"),
                    messages=[{"role": "user", "content": prompt}]
                )
                response_content = response.choices[0].message.content
                st.session_state.messages.append(
                    {"role": "assistant", "content": response_content}
                )
                st.write(response_content)
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.messages.pop()  # Remove user message if error occurs

# Add a clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

