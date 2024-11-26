# 프로젝트 이름

이 프로젝트는 FastAPI와 LangChain을 사용하여 다양한 언어 모델과 상호작용하는 웹 애플리케이션입니다.

## 요구사항
ollama 설치와 ollama로 실행할 model이 필요합니다. 이 프로젝트에서는 `EEVE-Korean-Instruct-10.8B-v1.0-Q8_0`와 `llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M` 를 테스트 하였습니다. 

## ollama에 모델 생성하기

### EEVE 다운로드 및 설치
EEVE는 야놀자에서 만든 모델입니다. `SOLAR`를기반으로 만들어 졌으며 한국어 학습이 되어 있는 모델입니다. ollama에서 실행하려면 gguf파일이 필요한데 테디노트님이 [로컬LLM호스팅 예제](https://youtu.be/VkcaigvTrug?si=rjrFVlDuPeFuGCiF) 만들어 올리신게 있습니다. [허깅페이스](https://huggingface.co/teddylee777/EEVE-Korean-Instruct-10.8B-v1.0-gguf/tree/main)에서 필요한 gguf 파일을 다운로드 받으시면 됩니다. 이 프로젝트는 `EEVE-Korean-Instruct-10.8B-v1.0-Q8_0.gguf` 를 사용했습니다.
`model/EEVE_Modelfile`내용을 보면 ollama 에서 모델을 생성하기 위한 설정 내용이 있습니다. 이 파일을 이용해 ollama에서 모델을 생성합니다.

```bash
ollama create EEVE-Korean-10.8B -f EEVE_Modelfile
# 생성 완료 후
ollama run EEVE-Korean-10.8B:latest
```

### Llama 3.2 다운로드 및 설치
meta에서 개발한 Llama 3.2도 사용해봤습니다. Llama는 한국어 학습이 안되어 있는 상태입니다. 허깅페이스에서 한국어 학습이된 Llama 3.2 gguf를 [다운로드](https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M/tree/main) 받습니다. EEVE처럼 ollama에 모델을 생성합니다.

```bash
ollama create llama-3.2-korean -f llama_Modelfile
# 생성 완료 후
ollama run llama-3.2-korean:latest
```

### ollama 특징
ollama는 모델을 사용하지 않으면 약 5분 뒤에 자동으로 모델이 종료 됩니다. 하지만 api 사용 시 자동으로 실행 되기 때문에 항상 run을 해두어야 할 필요는 없습니다.

## 개요

이 프로젝트는 FastAPI를 사용하여 웹 서버를 구축하고, LangChain을 사용하여 언어 모델과 상호작용합니다. 사용자는 다양한 언어 모델을 통해 번역, 대화, 그리고 기타 언어 처리 작업을 수행할 수 있습니다.

## 주요 기능

- **대화 기능**: 사용자가 AI와 대화할 수 있는 기능을 제공합니다.
- **번역 기능**: 입력된 텍스트를 다른 언어로 번역할 수 있는 기능을 제공합니다.
- **플레이그라운드**: 사용자가 다양한 언어 모델을 테스트할 수 있는 인터페이스를 제공합니다.

## 설치 방법

1. **가상 환경 생성 및 활성화**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

2. **필요한 패키지 설치**:
    ```bash
    pip install -r requirements.txt
    ```

3. **환경 변수 설정**:
    `.env` 파일을 생성하고 필요한 환경 변수를 설정합니다.
    ```properties
    TARGET_MODEL=your_model_name_here
    ```

## 사용 방법

1. **서버 실행**:
    ```bash
    cd app
    python server.py
    ```

2. **웹 브라우저에서 접속**:
    웹 브라우저를 열고 `http://localhost:8000`에 접속합니다.

3. **example**
    example 폴더는 RemoteRunnable을 사용하여 prompt, llm, translator에 접근하는 방법이 있습니다. 원격으로 llm에 접근하여 코드 레벨에서 원하는 작업을 할 수 있습니다.