import asyncio

from fastapi import APIRouter, HTTPException

from requests.login import LoginRequest

router = APIRouter(prefix="/user", tags=["user"])

@router.post(
    path="/login",
    tags=["user"],
    summary="Login user", description="Login user",
)
async def user_login(login: LoginRequest):
    try:

        return {'status': 'ok'}
    except Exception as e:
        raise HTTPException(status_code=500, detail={'error': str(e)})