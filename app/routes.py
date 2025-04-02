from fastapi import APIRouter, HTTPException

from app.data import backlogs
from app.models import Backlog

router = APIRouter()


@router.get("/backlogs", response_model=list[Backlog])
def list_backlogs():
    return backlogs


@router.post("/backlogs", response_model=Backlog)
def create_backlog(backlog: Backlog):
    backlogs.append(backlog)
    return backlog


@router.get("/backlogs/{backlog_id}", response_model=Backlog)
def get_backlog(backlog_id: str):
    for backlog in backlogs:
        if str(backlog.id) == backlog_id:
            return backlog
    raise HTTPException(status_code=404, detail="Backlog not found")


@router.delete("/backlogs/{backlog_id}")
def delete_backlog(backlog_id: str):
    for index, backlog in enumerate(backlogs):
        if str(backlog.id) == backlog_id:
            del backlogs[index]
            return {"detail": "Backlog deleted"}
    raise HTTPException(status_code=404, detail="Backlog not found")
