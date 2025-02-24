from fastapi import APIRouter

from app.api.ad import router as ad_router
from app.api.cmn import router as cmn_router

routers = APIRouter()

router_list = [
    ad_router,
    cmn_router,
]

for router in router_list:
    routers.include_router(router)
