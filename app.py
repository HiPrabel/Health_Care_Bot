import streamlit as st
import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")  

def healthcare_chatbot(user_input):
    with st.spinner("Processing, Please wait..."):
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
    return response.text

def main():
    st.set_page_config(page_title="Healthcare Assistant", page_icon="💊", layout="centered")

    st.markdown(
        """
        <style>
            .title {
                text-align: center;
                color: #4CAF50;
                font-size: 40px;
                font-weight: bold;
            }
            .message-box {
                background-color: #E8F5E9;
                padding: 15px;
                border-radius: 10px;
                color: #1B5E20;
                font-size: 18px;
            }
            .user-box {
                background-color: #E3F2FD;
                padding: 15px;
                border-radius: 10px;
                color: #0D47A1;
                font-size: 18px;
                text-align: right;
            }
            .chat-container {
                max-width: 600px;
                margin: auto;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='title'>🤖 Healthcare Assistant</h1>", unsafe_allow_html=True)

    user_input = st.text_input("💬 How may I assist you today?", key="user_input")

    if st.button("Submit"):
        if user_input.strip():
            response = healthcare_chatbot(user_input)

            st.markdown(f"<div class='chat-container'><p class='user-box'>👤 You: {user_input}</p></div>", unsafe_allow_html=True)
            
            st.markdown(f"<div class='chat-container'><p class='message-box'>🤖 Assistant: {response}</p></div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a message.")

if __name__ == "__main__":
    main()
