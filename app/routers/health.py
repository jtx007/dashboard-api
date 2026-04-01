from fastapi import APIRouter, Depends
from sqlmodel import Session, text

from app.database import get_session

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
def health_check():
    return {"status": "ok"}


@router.get("/db")
def db_check(session: Session = Depends(get_session)):
    session.exec(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
