from fastapi import APIRouter, HTTPException

router: APIRouter = APIRouter()


@router.put(
    path='/{path}',
    description='Endpunkt zum Weiterleiten von PUT-Anfragen an registrierte Services',
)
async def forward_put(path: str):
    try:
        return path
    except Exception:
        raise HTTPException(status_code=500)
