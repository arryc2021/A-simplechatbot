import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# Optional: use OpenAI or replace with another LLM
llm = ChatOpenAI(temperature=0)  # Needs OPENAI_API_KEY if used

def get_qa_chain():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain

def ask_agent(query: str) -> str:
    chain = get_qa_chain()
    try:
        return chain.run(query)
    except Exception as e:
        return f"❌ Error: {str(e)}"
