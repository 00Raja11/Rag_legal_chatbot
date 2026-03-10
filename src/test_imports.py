from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# Example retriever, replace with your actual retriever
retriever = ...  

prompt = PromptTemplate(
    input_variables=["question", "context"],
    template="Use the following context to answer the question:\n\n{context}\n\nQuestion: {question}\nAnswer:"
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt}
)