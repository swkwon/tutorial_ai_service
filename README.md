# 프로젝트 이름

이 프로젝트는 FastAPI와 LangChain을 사용하여 다양한 언어 모델과 상호작용하는 웹 애플리케이션입니다.

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
    example 폴더는 RemoteRunnable을 사용하여 prompt, llm, translator에 접근하는 방법이 있습니다.