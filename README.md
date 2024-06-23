# Backend-study

Backend-study 리포지토리는 Python을 사용하여 백엔드 개발을 공부하고 연습하기 위해 만들어졌습니다.

## 목차
- [소개](#소개)
- [시작하기](#시작하기)
  - [필수 조건](#필수-조건)
  - [설치](#설치)
- [사용법](#사용법)
  - [애플리케이션 실행](#애플리케이션-실행)
  - [테스트 실행](#테스트-실행)
- [프로젝트 구조](#프로젝트-구조)

## 소개
이 프로젝트는 백엔드 시스템을 구축하는 기술을 향상시키기 위해 다양한 예제와 연습 문제를 포함하고 있습니다. 주요 학습 내용은 다음과 같습니다:

- **Python FastAPI**: 비동기 웹 프레임워크를 사용하여 RESTful API를 구축하는 방법을 학습합니다.
- **Docker**: 애플리케이션을 컨테이너화하여 배포하고 관리하는 방법을 익힙니다.
- **Testing**: `pytest`를 사용하여 코드의 품질을 보장하고 유지보수를 쉽게 하는 방법을 연습합니다.
- **Database**: 데이터베이스와의 상호작용을 관리하고, SQLAlchemy를 사용하여 ORM을 구현합니다.

## 시작하기

### 필수 조건
- Python 3.8 이상
- Docker

### 설치
1. 리포지토리를 클론합니다:
    ```bash
    git clone https://github.com/SeongUk18/Backend-study.git
    cd Backend-study
    ```
2. Docker를 사용하여 애플리케이션을 빌드하고 실행합니다:
    ```bash
    docker-compose up --build
    ```

## 사용법

### 애플리케이션 실행
1. Docker 컨테이너를 빌드하고 실행합니다:
    ```bash
    docker-compose up --build
    ```
2. 애플리케이션이 실행되고 `http://localhost:8000`에서 접근 가능합니다.

### 테스트 실행
테스트를 실행하려면 다음 명령어를 사용하세요:
    ```bash
    docker-compose run backend pytest
    ```

## 프로젝트 구조
```markdown
Backend-study/
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── ...
├── .dockerignore
├── Dockerfile
├── docker-compose.yaml
├── pyproject.toml
└── README.md
