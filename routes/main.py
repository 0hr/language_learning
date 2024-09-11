from fastapi import APIRouter, HTTPException

from requests.login import LoginRequest

router = APIRouter()

@router.get(
    path="/",
    tags=["main"],
    summary="/", description="main",
)
async def main():
    return {'status': 'ok - working'}