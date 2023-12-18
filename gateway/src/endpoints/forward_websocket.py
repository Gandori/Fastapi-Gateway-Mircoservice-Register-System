from fastapi import APIRouter, HTTPException

router: APIRouter = APIRouter()


@router.websocket_route(
    path='/{path}',
)
async def forward_get(path: str):
    try:
        return path
    except Exception:
        raise HTTPException(status_code=500)
