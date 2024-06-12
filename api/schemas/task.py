from pydantic import BaseModel, Field
from typing import Optional


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, examples=["세탁소에 맡긴 것을 찾으러 가기"])


class TaskCreate(TaskBase):  # TaskBase를 변경하지 않으면 동작 확인 시 title이 표시되지 않음
    pass


class TaskCreateResponse(TaskCreate):
    id : int

    class Config:
        from_attributes = True


class Task(TaskBase):
    id : int
    done : bool = Field(False, description="완료 플래그")

    class Config:
        from_attributes = True
