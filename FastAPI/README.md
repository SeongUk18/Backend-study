# FastAPI

FastAPI 폴더는 FastAPI를 사용한 백엔드 개발을 학습하고 연습하는 내용을 포함하고 있습니다. 이 프로젝트는 Python을 사용하여 RESTful API를 구축하고, Docker로 배포하며, 데이터베이스와 상호작용하는 기술을 포함합니다.

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
이 프로젝트는 FastAPI를 사용한 비동기 웹 프레임워크 학습에 초점을 맞추고 있습니다. 주요 학습 내용은 다음과 같습니다:

- **Python FastAPI**: FastAPI를 사용한 RESTful API 구축
- **Docker**: 컨테이너화 및 배포
- **Testing**: `pytest`를 사용한 테스트 실행
- **Database**: SQLAlchemy를 사용한 데이터베이스 ORM

## 시작하기

### 필수 조건
- Python 3.8 이상
- Docker

### 설치
1. 리포지토리를 클론합니다:
    ```bash
    git clone https://github.com/SeongUk18/Backend-study.git
    cd Backend-study/FastAPI
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
    docker-compose run --entrypoint "poetry run pytest" demo-app
    ```

## 프로젝트 구조
```markdown
FastAPI/
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
