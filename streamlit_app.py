

import streamlit as st 
from utils import *
import component
from const import *
st.title(TITLE)

with st.sidebar:
    # Creating Sidebar
    model = st.selectbox(
        "Select the language model",
        MODEL_LIST,
    )
    temperature = st.slider(
        "Adjust the temperature",
        0.1, 1.0, 0.7, 0.01,
    )
    openai_api_key = st.text_input("API key",placeholder="OpenAi API key",type='password')
    system_prompt = st.text_area("Input your system prompt here",value=DEFAULT_SYSTEM_PROMPT,max_chars=2000)

if not (openai_api_key and system_prompt and model and temperature):
    assistant =  st.chat_message("assistant")
    assistant.write(ERROR_CONFIG_API_KEY)
else:
    try:
        conversation = create_llm_memory_chain(openai_api_key,system_prompt,temperature,model)
        put_message_on_screen()
        if user_prompt := st.chat_input("Say something"):
            user =  st.chat_message('user')
            user.markdown(user_prompt)
            response=conversation({"question": user_prompt})
            assistant =  st.chat_message('assistant')
            assistant.markdown(response.get("text"))
            st.session_state.messages=response.get("chat_history")
    except Exception as e:
            assistant =  st.chat_message('assistant')
            assistant.markdown(str(e))
component.get_footer()