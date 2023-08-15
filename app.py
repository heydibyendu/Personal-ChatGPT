# Import the Streamlit module
import streamlit as st

# Import LangChain modules
from langchain.chat_models import ChatOpenAI  
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Set page title and icon
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")

# Initialize session messages
if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Function to load the assistant's answer
def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer = chat(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content

# Create ChatOpenAI instance
chat = ChatOpenAI(temperature=0)

# Get user input and submit button
user_input = st.text_input("Ask me:")  # Text input field for user input
submit = st.button('Generate')  # Button labeled "Generate"

# Handle user input and display response
if submit:
    response = load_answer(user_input)  # Get the assistant's answer
    st.subheader("Answer:")  # Display a subheader titled "Answer:"
    st.write(response, key=1)  # Display the assistant's answer

# End of code