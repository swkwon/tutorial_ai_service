from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
target_model = os.getenv("EEVE_MODEL")
llm = ChatOllama(model=target_model)
prompt = ChatPromptTemplate.from_template("{topic}에 대해 간략히 설명해줘.")
chain = prompt | llm | StrOutputParser()
