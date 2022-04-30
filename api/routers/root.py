"""Define `root` API endpoint."""
from fastapi import APIRouter

from api.models import schemas


router = APIRouter()


@router.get("/", response_model=schemas.RootResponseBodySchema)
async def root() -> dict[str, str]:
    """Return a simple message."""
    return {"message": "Hello World!"}
