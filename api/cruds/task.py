from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema


def create_task(db: Session, task_create:task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.model_dump())
    db.add(task)
    db.commit() # db에 커밋
    db.refresh(task) # db 데이터를 바탕으로 task 인스턴스인 task를 업데이트 함
    return task # 생성한 db 모델 반환