
# 🧠 Serenity: Mental Health Chatbot Powered by LLaMA

Welcome to **Serenity**, an open-source mental health chatbot built with the LLaMA model family, Streamlit, and prompt engineering techniques. The goal is to offer a calm, empathetic, and informative digital companion—serving as a mental wellness support tool while remaining grounded in open, responsible AI development.

🌐 **Try the Demo**: [Launch the Chatbot](https://mental-health-chatbot-zjiawenz.streamlit.app/)  

---

## 📦 Project Features

- 🧘 **Empathetic Chatbot** persona with prompt-engineered emotional support
- 🧠 **Powered by LLaMA 3 (8B)** via Groq Cloud API for fast, cloud-hosted conversational capability
- 🖥️ **Streamlit-based Web Interface** for lightweight browser-based interaction
- 📚 **Future-ready** for cultural and emotional personalization, RAG memory, and fine-tuning

---

## 🚀 Future Product Vision

1. **Multi-Personality Support (Prompt Engineering):**
   
   - Introduce chatbot personas such as:
     - 🎎 **Dr. Mei Lin** – A compassionate female therapist rooted in East Asian cultural traditions. She emphasizes harmony, family values, and mindfulness in her therapeutic approach.
     - 🧔 **Dr. James Whitmore** – A thoughtful, analytical white male therapist trained in cognitive behavioral therapy. He offers structured, logical support with a calm, measured tone.   
     - 🧣 **Ms. Rosa Bennett** – A warm and nurturing counselor who speaks with maternal gentleness. She is especially attentive to emotional well-being and comfort.
     - 🌞 **Coach Leo Rivera** – An upbeat and energetic life coach with a focus on positivity, motivation, and action-oriented advice.
     - 🧘 **Monk Tashi** – A serene and wise mindfulness teacher drawing on Buddhist philosophy. He guides users through breathing, acceptance, and present-moment awareness.
     - 🎨 **Mx. Sage Quinn** – A creative, non-binary advisor who encourages emotional expression through art, journaling, and metaphorical thinking.

   - These personas will be invoked using carefully designed prompt templates to simulate tailored conversational styles and cultural sensitivity.
   
   - Users can choose their preferred persona on the chat interface.
   
   - This diversity acknowledges that healing often depends on feeling seen, understood, and culturally respected—especially when addressing trauma rooted in identity, history, or social context.

2. **Personalized Knowledge Base per User (RAG):**

   - Each user will have a private and persistent knowledge base that stores the emotional and biographical context shared during conversations. This may include:
     - Career history and professional obstacles
     - Personal relationships and interpersonal dynamics
     - Emotional patterns, self-described struggles, and growth milestones
     - Communication styles and preferred tones
   
   - Upon return, the chatbot will recall past interactions to offer more meaningful, context-aware, and emotionally attuned support.
   
   - Future plans include integrating this knowledge base with a retrieval-augmented generation (RAG) module to allow the chatbot to “remember” and refer to previous sessions in a personalized, healing-centered dialogue.
   
   - The goal is to simulate the therapeutic continuity found in human counseling—where a therapist remembers your story, notices your progress, and builds trust over time.

3. **Fine-Tuning the Model:**
   - If relevant domain-specific mental health dialog data is available, fine-tune the base model using parameter-efficient methods (e.g., LoRA).
   - The objective is to improve alignment with therapeutic dialogue goals and increase personalization.

---

## 📅 Project History

### [2025-04-23] Switched from Ollama to Groq API
- Removed local dependency on `ollama.Client()`
- Integrated Groq-hosted LLaMA 3 (8B) via `requests`
- Updated prompt to structured, persona-based system message
- Transitioned from local-only development to Streamlit Cloud deployment
- App is now accessible via public URL with cloud-based hosting and automatic builds

### [2025-04-21] Initial Commit
- Local inference using `llama.cpp` with 4-bit quantized LLaMA 2 7B Chat model
- Prompt engineering to simulate an emotionally supportive therapist assistant
- Streamlit-based UI for lightweight demo
- Implemented session-based chat flow
- Added assistant typing animation with `time.sleep()`

---

## 📫 Contact

For questions, please contact:
**Jiawen Zou** · E-mail: [annajzou@gmail.com] · GitHub: [@zjiawenz](https://github.com/zjiawenz)
