# from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema


async def create_task(db: AsyncSession, task_create:task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.model_dump())
    db.add(task)
    # db.commit() # db에 커밋
    # db.refresh(task) # db 데이터를 바탕으로 task 인스턴스인 task를 업데이트 함
    await db.commit()
    await db.refresh(task)
    return task # 생성한 db 모델 반환


async def get_tasks_with_done(db: AsyncSession) -> list[tuple[int, str, bool]]:
    result:Result = await db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Task.due_date,
            task_model.Done.id.isnot(None).label("done"),
        ).outerjoin(task_model.Done)
    )

    return result.all()


async def get_task(db: AsyncSession, task_id: int) -> task_model.Task:
    result:Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    return result.scalars().first()


async def update_task(
        db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
    )  -> task_model.Task:
    original.title = task_create.title
    original.due_date = task_create.due_date
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()
