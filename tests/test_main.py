import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import starlette.status

from api.db import get_db, Base
from api.main import app


ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    # 비동기식 DB 접속을 위한 엔진과 세션을 작성
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )

    # 테스트용으로 온 메모리 SQLite 테이블을 초기화 (함수별로 재설정)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


    # 의존성 주입으로 FastAPI가 테스트용 DB를 참조하도록 변경
    async def get_test_db():
        async with async_session() as session:
            yield session

    
    app.dependency_overrides[get_db] = get_test_db

    # 테스트 용으로 비동기 HTTP 클라이언트 반환
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client



@pytest.mark.asyncio
async def test_create_and_read(async_client):
    response = await async_client.post("/tasks", json={"title": "테스트 작업"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert "id" in response_obj
    assert response_obj["title"] == "테스트 작업"


@pytest.mark.asyncio
async def test_done_flag(async_client):
    # Create a new task
    response = await async_client.post("/tasks", json={"title": "테스트 작업2"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert "id" in response_obj
    assert response_obj["title"] == "테스트 작업2"

    task_id = response_obj["id"]

    # 완료 플래그 설정
    response = await async_client.put(f"/tasks/{task_id}/done")
    assert response.status_code == starlette.status.HTTP_200_OK

    # 이미 완료 플래그가 설정되어 있으므로 400을 반환
    response = await async_client.put(f"/tasks/{task_id}/done")
    assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST

    # 완료 플래그 해제
    response = await async_client.delete(f"/tasks/{task_id}/done")
    assert response.status_code == starlette.status.HTTP_200_OK

    # 이미 완료 플래그가 해제되었으므로 404 반환
    response = await async_client.delete(f"/tasks/{task_id}/done")
    assert response.status_code == starlette.status.HTTP_404_NOT_FOUND
