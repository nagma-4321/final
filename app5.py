
print("hello")

import streamlit as st

# Initialize session state for chatbot state
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Stores chat messages

# Define chatbot questions
questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you get a chance to write a book regarding the philosophy of living life, what would be the title?",
    "Do you pay gratitude to the higher for all the opportunities in your life?",
    "What one advice do you want to give yourself to be happier in life?"
]

# Suggestion after Question 7
suggestion = "Please convert them to physical copies; otherwise, you might lose them due to storage issues."

# Layout configuration
st.set_page_config(page_title="DATE TO MEMORIES (2024 Edition)", layout="wide")

# Styling for the header
st.markdown(
    """
    <div style="background-color:orange; padding:20px; border-radius:10px; text-align:center;">
        <h1 style="color:white; margin:0;">DATE TO MEMORIES (2024 Edition)</h1>
        <h3 style="color:white; margin:0;">Reliving Moments, Creating Memories</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chat container
st.write("### Chat")
chat_area = st.empty()

# Input area
user_input = st.text_input("Type your response and press Enter:")


# Helper function to render chat
def display_chat():
    """Render the chat history in WhatsApp-style chat bubbles."""
    chat_html = ""
    for message in st.session_state.chat_history:
        if message["sender"] == "bot":
            # Bot's message
            chat_html += f"""
            <div style="text-align:left; margin:10px;">
                <div style="display:inline-block; padding:10px; background-color:#f0f0f0; border-radius:10px; max-width:60%; font-family:sans-serif;">
                    <b>Bot:</b> {message['text']}
                </div>
            </div>
            """
        else:
            # User's message
            chat_html += f"""
            <div style="text-align:right; margin:10px;">
                <div style="display:inline-block; padding:10px; background-color:#e1ffc7; border-radius:10px; max-width:60%; font-family:sans-serif; font-weight:bold;">
                    {message['text']}
                </div>
            </div>
            """
    chat_area.markdown(chat_html, unsafe_allow_html=True)


# Main logic for handling chat
if user_input:
    # Record user input
    st.session_state.chat_history.append({"sender": "user", "text": user_input})

    # Get the current question
    current_index = st.session_state.current_question_index
    if current_index < len(questions):
        # Store response and advance to next question
        st.session_state.chat_history.append({"sender": "bot", "text": questions[current_index]})
        st.session_state.current_question_index += 1
    elif current_index == 7:
        # Add suggestion after question 7
        st.session_state.chat_history.append({"sender": "bot", "text": suggestion})
        st.session_state.current_question_index += 1
    else:
        # End of chat
        user_name = st.session_state.chat_history[0].get("text", "Friend")
        thank_you_message = (
            f"Thank you for your responses, {user_name}! I appreciate your thoughtful answers and wish you the best for the future."
        )
        st.session_state.chat_history.append({"sender": "bot", "text": thank_you_message})

    # Clear input box for next response
    st.session_state.user_input = ""
    st.experimental_rerun()

# Render chat history
display_chat()

# If there are remaining questions, show the next one
if st.session_state.current_question_index < len(questions):
    st.session_state.chat_history.append(
        {"sender": "bot", "text": questions[st.session_state.current_question_index]}
    )





        