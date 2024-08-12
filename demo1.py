import streamlit as st

# Streamlit layout
st.set_page_config(page_title="MediCore - Empathetic Mental Health Companion", layout="wide")

st.markdown("""
<style>
body {
    background-color: white;
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
messages = []

# User input
user_input = st.chat_input("")

# Display the chat history
with chat_history.container():
    for message in messages:
        st.write(message)

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 336px; /* Adjust this value to match the width of your sidebar */
        width: calc(100% - 336px); /* Adjust this value to match the width of your sidebar */
        text-align: center; /* Center text within the available width */
        color: grey;
        padding: 10px;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        background: white; /* Ensure footer background is white to match the page background */
    }
    </style>
    <div class="footer">
        Created by the Innovative Sparks. This chatbot does not replace human interaction. Seek help from nearby facilities.
    </div>
    """,
    unsafe_allow_html=True
)
