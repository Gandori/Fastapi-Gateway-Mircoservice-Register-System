from fastapi import APIRouter, HTTPException

router: APIRouter = APIRouter()


@router.get(
    path='/{path}',
    description='Endpunkt zum Weiterleiten von GET-Anfragen an registrierte Services',
)
async def forward_get(path: str):
    try:
        return path
    except Exception:
        raise HTTPException(status_code=500)
