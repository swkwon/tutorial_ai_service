from langserve import RemoteRunnable
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = RemoteRunnable("http://localhost:8000/llm")

prompt = ChatPromptTemplate.from_template(
    "다음 내용을 여학생이 하는 말처럼 꾸며줘:\n{topic}"
)

chain = prompt | llm | StrOutputParser()
for token in chain.stream({"topic": "오늘은 날씨가 비가 옵니다. 감성적이네요. 우산챙기세요."}):
    print(token, end="")