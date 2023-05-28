import datetime

from pydantic import BaseModel, validator

from routes.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    question: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    question: str
    content: str

    @validator('question', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class QuestionList(BaseModel):
    total:int = 0
    question_list : list[Question] = []