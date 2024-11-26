from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
target_model = os.getenv("TARGET_MODEL")
llm = ChatOllama(model=target_model)

prompt = ChatPromptTemplate.from_template(
    "Translate following sentences into Korean:\n{input}"
)

chain = prompt | llm | StrOutputParser()
