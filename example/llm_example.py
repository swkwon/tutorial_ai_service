from langserve import RemoteRunnable
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = RemoteRunnable("http://localhost:9100/llm")

prompt = ChatPromptTemplate.from_template(
    "다음 내용을 SNS에 올리는 글처럼 만들어줘.:\n{topic}"
)

chain = prompt | llm | StrOutputParser()
for token in chain.stream({"topic": "오늘은 날씨가 비가 옵니다. 우산이 필요힙니다."}):
    print(token, end="")