from fastapi import APIRouter

from api.v1.endpoints import vuttr


api_router = APIRouter()
api_router.include_router(vuttr.router, prefix='/vuttr', tags=['vuttr'])