from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/prompt")

for token in chain.stream({"topic": "하와이 30일 일정을 계획해줘."}):
    print(token, end="") 