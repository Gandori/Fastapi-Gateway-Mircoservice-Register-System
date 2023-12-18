from fastapi import APIRouter, HTTPException

router: APIRouter = APIRouter()


@router.delete(
    path='/{path}',
    description='Endpunkt zum Weiterleiten von DELETE-Anfragen an registrierte Services',
)
async def forward_delete(path: str):
    raise HTTPException(status_code=500)

    try:
        return path
    except Exception:
        raise HTTPException(status_code=500)
