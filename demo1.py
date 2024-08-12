import streamlit as st

# Streamlit layout
st.set_page_config(page_title="MediCore - Empathetic Mental Health Companion", layout="wide")

# Apply custom styles
st.markdown("""
<style>
body {
    background-color: #003366; /* Dark blue background color */
    color: #ffffff; /* White text color for better contrast */
    margin: 0;
    padding: 0;
}
.sidebar .sidebar-content {
    background-color: #003366; /* Dark blue for the sidebar */
    color: #ffffff; /* White text color for sidebar content */
}
.sidebar .sidebar-header {
    background-color: #003366; /* Ensure the header of the sidebar is the same color */
    color: #ffffff; /* White text color for the sidebar header */
}
h1, h2, h3, h4, h5, h6, p {
    color: #ffffff; /* Ensure text is visible on dark background */
}
.chat-container {
    padding: 20px;
    border-radius: 8px;
    background-color: #00509e; /* Lighter blue for chat container */
}
.input-container {
    background-color: #ff69b4; /* Pink background color for chat input area */
    padding: 10px;
    border-radius: 8px;
}
.input-container input {
    width: calc(100% - 110px); /* Adjust input field width */
    padding: 10px;
    border: none;
    border-radius: 4px;
}
.input-container button {
    width: 100px;
    background-color: #ffffff; /* White button background */
    color: #ff69b4; /* Pink button text */
    border: none;
    border-radius: 4px;
    padding: 10px;
    cursor: pointer;
}
.input-container button:hover {
    background-color: #ff85c0; /* Lighter pink on hover */
}
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: center;
    color: #003366;
    padding: 10px;
    box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
    background: #ffffff; /* White background for the footer */
}
</style>
""", unsafe_allow_html=True)

# Sidebar for mood checkboxes
st.sidebar.title("How do you feel today?")
feeling_anxious = st.sidebar.checkbox("Feeling Anxious")
feeling_depressed = st.sidebar.checkbox("Feeling Depressed")
feeling_stressed = st.sidebar.checkbox("Feeling Stressed")
trouble_sleeping = st.sidebar.checkbox("Trouble Sleeping")

# Chat interface
st.title("MediCore")

# Chat history container
chat_history = st.empty()

# Placeholder for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

def add_message(user_input, response):
    st.session_state.messages.append(f"**You:** {user_input}")
    st.session_state.messages.append(f"**MediCore:** {response}")

# Display the chat history
with chat_history.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for message in st.session_state.messages:
        st.write(message)
    st.markdown('</div>', unsafe_allow_html=True)

# Chat input area with pink background
st.markdown("""
<div class="input-container">
    <form action="#" method="post">
        <input type="text" id="user_input" name="user_input" placeholder="Your message here:" />
        <button type="submit">Send</button>
    </form>
</div>
""", unsafe_allow_html=True)

# Handle form submission
user_input = st.text_input("Your message here:", key="input")
if st.button('Send'):
    if user_input:
        # For demonstration purposes, we use a simple echo response
        response = f"I hear you saying: '{user_input}'"
        add_message(user_input, response)
    else:
        st.warning("Please enter a message before sending.")

# Footer
st.markdown(
    """
    <div class="footer">
        Created by the Innovative Sparks. This chatbot does not replace human interaction. Seek help from nearby facilities.
    </div>
    """,
    unsafe_allow_html=True
)
