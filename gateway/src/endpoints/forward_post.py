from fastapi import APIRouter, HTTPException

router: APIRouter = APIRouter()

# '/register-microservice',


@router.post(
    path='/{path}',
    description='Endpunkt zum Weiterleiten von GET-Anfragen an registrierte Services',
)
async def forward_get(path: str):
    try:
        return path
    except Exception:
        raise HTTPException(status_code=500)
