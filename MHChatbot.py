import streamlit as st
import time
import ollama

st.markdown(
    """ 
    Hi there 👋 and welcome to **Serenity**, your supportive mental health companion. 
    
    I am here to provide a safe, non-judgmental space where you can:

    💭 Talk about what’s on your mind
    
    🌿 Receive calming tips for stress or anxiety
    
    📝 Get journaling prompts and mindfulness ideas
    
    🤝 Feel heard, supported, and not alone
    """
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi I'm Serenity. How's everything going?"}]

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept new user input
if prompt := st.chat_input("How do you feel today?"):
    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build full conversation context for the model
    conversation_history = ""
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Serenity"
        conversation_history += f"{role}: {msg['content']}\n"

    # Call the model using the full context
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            client = ollama.Client()
            response = client.generate(model="mhgeneral", prompt=conversation_history)

            for chunk in response.response.split():
                full_response += chunk + " "
                time.sleep(0.03)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = "⚠️ Error talking to Serenity: " + str(e)
            message_placeholder.markdown(full_response)

    # Append assistant's response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
