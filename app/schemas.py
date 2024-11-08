from pydantic import BaseModel


class TokenRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class UserResponse(BaseModel):
    username: str
    email: str
    role: str

    class Config:
        orm_mode = True 
