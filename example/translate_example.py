from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:9100/translator")

for token in chain.stream({"input": "Hello, how are you?"}):
    print(token, end="")