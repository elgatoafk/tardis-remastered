import timedelta
from pydantic import BaseModel


class TimeDiffRequest(BaseModel):
    datetime_str: str
    timezone: str


class TimeDeltaRequest(BaseModel):
    datetime_str: str
    timedelta_days: int
