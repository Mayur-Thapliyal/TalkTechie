import streamlit as st
from const import GREETING_MSG
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI,OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema.messages import (HumanMessage,AIMessage,SystemMessage)
from langchain.prompts import (ChatPromptTemplate,MessagesPlaceholder,SystemMessagePromptTemplate,HumanMessagePromptTemplate,)

def put_message_on_screen()->(None):
    """
    This function is used to put user messages on the screen if there are any in streamlit session memory
    """
    if "messages" not in st.session_state:
        st.session_state["messages"]= [AIMessage(content=GREETING_MSG)]
    for message in st.session_state.messages:
            role =  "user" if isinstance(message,HumanMessage) else "assistant" if isinstance(message,AIMessage)  else None
            if role:
                with st.chat_message(role):
                    st.markdown(message.content)
                    
@st.cache_resource
def create_llm_memory_chain(api_key: str,system_prompt: str,temperature: float,model: str)->(LLMChain):
    """This function create a LangChain OpenAI LLM_chain that can store user conversation.
    @st.cache_resource cache the resources preventing this function to execute again and again when ever something is changed in screen and streamlit re-render,
    this store the resources in cache creating stable connection unless function params are changed
    Args:
        api_key (OpenAI_API_KEY): User Open API key
        system_prompt: System prompt to change the bot behavior 
        temperature:  text randomness, lower values produce conservative outputs, higher values result in diversity.
        model: OpenAi model you want to use
    Returns:
        LLMChain: a LLMChain Object that can automatically save user messages into the local memory
    """
    llm = ChatOpenAI(api_key=api_key,temperature=temperature,model=model)
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                system_prompt
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}")
        ]
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory
    )
    return conversation