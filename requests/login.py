from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., description="username")
    password: str = Field(..., description="password")