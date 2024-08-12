import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Chatbot", page_icon="🤖")

# Custom CSS to style the background color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #E0F7FA; /* Light blue background */
    }
    .sidebar .sidebar-content {
        background-color: #E0F7FA; /* Light blue background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to simulate chatbot responses
def get_bot_response(user_input):
    # This is where you can implement a more sophisticated chatbot logic
    # For now, it just echoes the user input
    return f"You said: {user_input}"

# Streamlit app layout
st.title("Simple Chatbot")

# Text input for user messages
user_input = st.text_input("You:", "")

# Display chat history
if user_input:
    response = get_bot_response(user_input)
    st.write(f"**Chatbot:** {response}")

# Note: For a more interactive chat, you might use session state to manage chat history
