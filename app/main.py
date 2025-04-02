from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Nomad",
    description="A Python FastAPI microservice that manages Agile backlogs",
)

app.include_router(router)
