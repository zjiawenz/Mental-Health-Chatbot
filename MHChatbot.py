import streamlit as st
import time
import requests

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

# Load your Groq API key from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]

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

    # Construct API-compatible message list
    formatted_messages = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state.messages
    ]

    # Send to Groq
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "system", "content": "You are a compassionate therapist helping users feel better."}] + formatted_messages,
        "temperature": 0.7
    }

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            reply = response.json()["choices"][0]["message"]["content"]

            # Animate response word-by-word
            for word in reply.split():
                full_response += word + " "
                time.sleep(0.03)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = "⚠️ Error talking to Serenity: " + str(e)
            message_placeholder.markdown(full_response)

    # Append assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

