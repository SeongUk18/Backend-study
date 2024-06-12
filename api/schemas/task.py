from pydantic import BaseModel, Field
from typing import Optional


class Task(BaseModel):
    id : int
    title: Optional[str] = Field(None, example="세탁소에 맡긴 것을 찾으러 가기")
    done : bool = Field(False, description="완료 플래그")

