import timedelta
from pydantic import BaseModel
from datetime import timedelta


class TimeDiffRequest(BaseModel):
    datetime_str: str
    timezone: str


class TimeDeltaRequest(BaseModel):
    datetime_str: str
    timedelta: timedelta
