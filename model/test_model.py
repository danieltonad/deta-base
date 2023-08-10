from pydantic import BaseModel, EmailStr

class TestModel(BaseModel):
    id: str
    email: EmailStr

class TestRequest(BaseModel):
    email: EmailStr