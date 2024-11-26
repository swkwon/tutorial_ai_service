# 프로젝트 이름
이 프로젝트는 FastAPI와 LangChain을 사용하여 다양한 언어 모델과 상호작용하는 웹 애플리케이션입니다.

## 요구사항
ollama 설치와 model이 필요합니다. 모델은 한국어가 학습된 `llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M.gguf` 를 사용 하였습니다. 

## ollama에 모델 생성하기

### Llama 3.2 다운로드 및 설치
허깅페이스에서 Llama 3.2 한국어 학습된 버전 `llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M.gguf`을 [다운로드](https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M/tree/main) 합니다. 다운로드한 gguf 파일은 model 폴더로 옮깁니다.
`ollama create` 하기 위해서는 gguf 파일이 필요합니다.

### ollama model 생성
```bash
cd model # model 폴더 안에 llama 용 Modelfile이 있습니다.
ollama create llama-3.2-korean -f llama_Modelfile # llama-3.2-korean 이라는 이름으로 ollama 모델이 생성됩니다.
# 생성 완료 후
ollama run llama-3.2-korean:latest # 모델을 실행해서 테스트를 해볼 수 있습니다.
```

### ollama 특징
꼭 `ollama run`을 안하더라고 langchain으로 모델을 사용할 때 자동으로 시작됩니다.

## 개요
이 프로젝트는 FastAPI를 사용하여 웹 서버를 구축하고, langchain을 사용하여 언어 모델과 상호작용합니다. 사용자는 다양한 언어 모델을 통해 번역, 대화, 그리고 기타 언어 처리 작업을 수행할 수 있습니다.

## 주요 기능

- **대화 기능**: 사용자가 AI와 대화할 수 있는 기능을 제공합니다.
- **번역 기능**: 입력된 텍스트를 다른 언어로 번역할 수 있는 기능을 제공합니다.
- **플레이그라운드**: 사용자가 다양한 언어 모델을 테스트할 수 있는 인터페이스를 제공합니다.

## 설치 방법

1. **가상 환경 생성 및 활성화**:
    ```bash
    # 반드시 해야되는 부분은 아닙니다.
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

2. **필요한 패키지 설치**:
    ```bash
    pip install -r requirements.txt
    ```

## 사용 방법

1. **서버 실행**:
    ```bash
    cd app
    python server.py
    ```

2. **웹 브라우저에서 접속**:
    웹 브라우저를 열고 `http://localhost:8000`에 접속합니다. `server.py`를 보면 루트 url로 접속 시 `/chat/playground` 로 redirect 됩니다.

3. **example 폴더**:
    example 폴더는 langserve RemoteRunnable을 사용하여 prompt, llm, translator에 접근하는 방법이 있습니다. 원격으로 llm에 접근하여 코드 레벨에서 원하는 작업을 할 수 있습니다.