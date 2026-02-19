from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import  os
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(
    model="openai/gpt-5.2-chat",
    openai_api_key=os.environ["OPENAI_API_KEY"],
    openai_api_base=os.environ["OPENAI_BASE_URL"],
)
prompt = ChatPromptTemplate.from_template("""
You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Keep the answer concise.

Context: {context}
Question: {question}

Answer:
""")

generation_chain = prompt | llm | StrOutputParser()