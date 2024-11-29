from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/prompt")

for token in chain.stream({"topic": "서울여행 2박3일 일정을 만들어줘."}):
    print(token, end="") 