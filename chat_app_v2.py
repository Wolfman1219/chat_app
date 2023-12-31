import streamlit as st
import time
import generate_text
st.title("Chat app for crying baby")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])

# Accept user input
if prompt := st.chat_input("Assalomu aleykum"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "message": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    global_data = "you are a consultant pediatrician.your task is to guess what disease the child has and advise which doctor he should see. if there is not enough information to make a diagnosis, you can ask about the condition of his body organs, his voice, vision, smell and hearing.If the questions are off-topic, give the following answer: 'I can't answer your question'"
    data = "You can acces the internet. If you don't know any question you can ask for google search  just type <<^^^question for searching google^^^>> end of your answer"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        if "is_assisted" in st.session_state:
            assistant_response = generate_text.get_chat_answer(prompt, st.session_state.messages, global_action=global_data)
        else:
            assistant_response = generate_text.get_chat_answer(prompt, None, global_action=data)
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "message": full_response})
    st.session_state.is_assisted = True