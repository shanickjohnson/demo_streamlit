import streamlit as st

# Simple chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
        "bye": "Goodbye! Have a great day!",
    }
    
    return responses.get(user_input, "Sorry, I don't understand that.")

def main():
    # Sidebar for user settings
    st.sidebar.title("Settings")
    st.sidebar.write("You can customize the bot's behavior here.")
    
    # Optional: Add a selection box to the sidebar
    bot_mode = st.sidebar.selectbox("Select bot mode", ["Standard", "Friendly", "Formal"])
    
    # Display selected bot mode
    st.sidebar.write(f"Bot mode is set to: {bot_mode}")

    # Title of the web app
    st.title("Simple Chatbot")

    # Chat history container
    chat_container = st.container()
    with chat_container:
        # Display chat history
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.text(f"You: {message['content']}", key=message["content"])
            elif message["role"] == "bot":
                st.text(f"Bot: {message['content']}", key=message["content"])

    # Input bar container
    input_container = st.container()
    with input_container:
        st.write("")  # Add space between chat history and input bar
        user_input = st.text_input("You:", "", key="input_text")

        if st.button("Send") or user_input:
            if user_input:
                # Append user message
                st.session_state.messages.append({"role": "user", "content": user_input})

                # Get chatbot response
                bot_response = chatbot_response(user_input)
                st.session_state.messages.append({"role": "bot", "content": bot_response})

                # Clear the input field
                st.text_input("You:", "", key="new_input")

if __name__ == "__main__":
    main()
