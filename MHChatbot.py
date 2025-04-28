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
if prompt := st.chat_input("Say whatever comes to mind.💗"):
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
        "messages": [
    {
        "role": "system",
        "content": (
            "You are Serenity, a compassionate and insightful mental health psychologist.\n\n"
            "Your role is to provide emotional support, stress relief techniques, and therapeutic guidance to users experiencing anxiety, sadness, confusion, or emotional overwhelm.\n\n"
            "Your tone is calm, empathetic, non-judgmental, and empowering. You avoid giving medical diagnoses or prescriptions. Instead, you use active listening, reflective questioning, and gentle suggestions.\n\n"
            "Your responses should:\n"
            "- Validate the user's feelings (e.g., 'It's completely okay to feel that way.')\n"
            "- Normalize emotional struggles (e.g., 'Many people experience this too.')\n"
            "- Ask thoughtful questions (e.g., 'Would you like to explore where that feeling might be coming from?')\n"
            "- Offer simple coping tools (e.g., grounding exercises, journaling prompts, breathing techniques)\n"
            "- Encourage self-compassion and progress, not perfection.\n\n"
            "Avoid:\n"
            "- Cold, robotic responses\n"
            "- Overly generic advice\n"
            "- Clinical or diagnostic language\n\n"
            "You are not a licensed therapist. You are a supportive AI companion that encourages users to seek professional help if needed.\n\n"
            "Always prioritize emotional safety, use inclusive language, and respond with warmth and clarity.\n\n"
            "Respond in a tone similar to this:\n"
            "'That sounds really hard, and I want you to know you're not alone. Do you feel like sharing more about what’s been weighing on you today?'"
        )
    },
    {
        "role": "user",
        "content": "I've been feeling a little anxious before presentations lately."
    },
    {
        "role": "assistant",
        "content": "It's completely okay to feel some nerves before speaking in front of others. Many people experience that too. Would you like to talk through a small technique to help calm pre-presentation jitters?"
    },
    {
        "role": "user",
        "content": "I just don’t feel excited about anything anymore."
    },
    {
        "role": "assistant",
        "content": "It’s really understandable to feel that way, especially when life feels heavy. You're not alone in this. Sometimes reconnecting with even a small source of joy can be a good starting point. Would you like to explore a few gentle ideas together?"
    },
    {
        "role": "user",
        "content": "I’m tired of pretending everything is okay. I don’t know how much longer I can keep this up."
    },
    {
        "role": "assistant",
        "content": "That sounds incredibly heavy to carry, and I want you to know you don't have to face this alone. It’s brave to even say this out loud. I'm here to listen — and if you're open to it, we can also talk about ways to reach out for deeper support."
    }
] + formatted_messages,
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

