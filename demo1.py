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
    background-color: #00509e; /* Lighter blue for the sidebar */
}
h1, h2, h3, h4, h5, h6, p {
    color: #ffffff; /* Ensure text is visible on dark background */
}
.chat-container {
    padding: 20px;
    border-radius: 8px;
    background-color: #00509e; /* Ensure chat container background is visible */
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

# User input
user_input = st.text_input("Your message here:", key="input")

if st.button('Send'):
    if user_input:
        # For demonstration purposes, we use a simple echo response
        response = f"I hear you saying: '{user_input}'"
        add_message(user_input, response)
        st.session_state.messages.append(f"**You:** {user_input}")
        st.session_state.messages.append(f"**MediCore:** {response}")
    else:
        st.warning("Please enter a message before sending.")

# Display the chat history
with chat_history.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for message in st.session_state.messages:
        st.write(message)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        Created by the Innovative Sparks. This chatbot does not replace human interaction. Seek help from nearby facilities.
    </div>
    """,
    unsafe_allow_html=True
)
