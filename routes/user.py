from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from requests.login import LoginRequest
from services.login_service import LoginService, login_service

router = APIRouter(prefix="/user", tags=["user"])

@router.post(
    path="/login",
    tags=["user"],
    summary="Login user", description="Login user",
)
async def user_login(login: LoginRequest, login_service: LoginService = Depends(login_service)):
    try:
        if login_service.login(login.username, login.password):
            return {'status': 'login successfully'}
        return {'status': 'login failed'}
    except Exception as e:
        raise HTTPException(status_code=500, detail={'error': str(e)})