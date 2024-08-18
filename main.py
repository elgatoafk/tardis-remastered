import os
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from backend.src.routes import admin, user
from fastapi import FastAPI
import uvicorn
from backend.src.util.db import init_db, SessionLocal
from backend.src.util.models import TimeZone

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(user.router, prefix="/user", tags=["user"])


def insert_default_timezones(db: Session):
    timezones = [
        {"name": "America/New_York", "is_default": True},
        {"name": "Europe/Kyiv", "is_default": True},
        {"name": "Asia/Calcutta", "is_default": True},
        {"name": "Etc/UTC", "is_default": True},
    ]

    for tz in timezones:
        existing_tz = db.query(TimeZone).filter(TimeZone.name == tz["name"]).first()
        if not existing_tz:
            db.add(TimeZone(name=tz["name"], is_default=tz["is_default"]))

    db.commit()


@app.on_event("startup")
async def startup():
    init_db()
    db = SessionLocal()
    try:
        insert_default_timezones(db)
    finally:
        db.close()


if __name__ == "__main__":
    debug_mode = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=debug_mode)
