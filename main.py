import streamlit as st
from streamlit_chat import message
import pinecone
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone


embeddings = OpenAIEmbeddings()

# initialize pinecone
pinecone.init(
    api_key=str(os.environ['7097682e-9631-4b87-98fa-704c5ea7097f']),  # find at app.pinecone.io
    environment=str(os.environ['us-west4-gcp-free'])  # next to api key in console
)

index_name = str(os.environ['law-agent'])

# Backend / langchain
def load_chain():
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    return docsearch

chain = load_chain()

# From here down is all the StreamLit UI.
st.set_page_config(page_title="Law Agent", page_icon=":robot:")
st.header("Law Agent")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text


user_input = get_text()

if user_input:
    docs = chain.similarity_search(user_input)
    output = docs[0].page_content

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")