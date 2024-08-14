from datetime import datetime, timedelta
from dateutil import tz
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from backend.src.util.schemas import TimeDiffRequest, TimeDeltaRequest
from backend.src.services.tardis import TardisService
from backend.src.util.db import get_db
from backend.src.util.models import TimeZone

router = APIRouter()


@router.get("/timezones/")
def get_all_timezones(db: Session = Depends(get_db)):
    """
    Retrieve all timezones from the database.

    This route fetches all the timezone entries stored in the database and returns them
    as a JSON response. If there are no timezones found, an empty list is returned.

    Args:
        db (Session): The SQLAlchemy database session used to interact with the database.

    Returns:
        JSONResponse: A JSON response containing a list of all timezones stored in the database.
                      Each timezone is represented by its name.
    """
    timezones = db.query(TimeZone).all()

    if not timezones:
        return JSONResponse({"timezones": []}, status_code=200)

    timezone_list = [timezone.name for timezone in timezones]
    return JSONResponse({"timezones": timezone_list}, status_code=200)


@router.post("/get-difference")
async def calculate_time_diff(request: TimeDiffRequest):
    """
    Calculates the time difference between the current UTC time and a user-provided datetime.

    This endpoint accepts a datetime string and a timezone from the user, converts the input into a
    timezone-aware datetime object, and calculates the time difference between the user's input and
    the current UTC time. If the user's input is in the future, it formats the difference accordingly
    and returns a warning.

    Args:
        request (TimeDiffRequest): A Pydantic model containing:
            - datetime_str (str): The user's input datetime as a string.
            - timezone (str): The timezone of the user's input.

    Returns:
        JSONResponse: A JSON response containing:
            - calculated_from (str): The formatted input datetime string.
            - result (str): The formatted time difference.
            - future_warning (bool): Indicates whether the input datetime is in the future.
    """
    try:

        formatted_input = TardisService.convert_to_datetime(request.datetime_str, request.timezone)
    except HTTPException as http_exc:
        raise http_exc

    current_time = datetime.now(tz=tz.UTC)
    passing_input = TardisService.format_to_string(formatted_input)

    if formatted_input > current_time:
        result = TardisService.calculate_difference(formatted_input, current_time)
        formatted_result = TardisService.format_results(result, TardisService.RESULT_FORMAT_FUTURE)
        return JSONResponse(
            {"calculated_from": passing_input, "result": formatted_result, "future_warning": True},
            status_code=200
        )

    result = TardisService.calculate_difference(current_time, formatted_input)
    formatted_result = TardisService.format_results(result)
    return JSONResponse(
        {"calculated_from": passing_input, "result": formatted_result, "future_warning": False},
        status_code=200
    )


@router.post("/add-subtract-timedelta")
async def get_new_date(request: TimeDeltaRequest):
    """
       Adds or subtracts a timedelta to/from a given datetime and returns the resulting datetime.

       Args:
           request (TimeDeltaRequest): A Pydantic model containing:
               - datetime_str (str): The user's input datetime as a string
               - days (int): Number of days to add/subtract (default: 0).

       Returns:
           JSONResponse: A JSON response containing:
               - result (str): The resulting datetime as a formatted string.

       """
    try:
        formatted_input = TardisService.convert_to_datetime(request.datetime_str)
    except HTTPException as http_exc:
        raise http_exc
    user_timedelta = timedelta(days=request.timedelta_days)
    result = TardisService.add_timedelta(formatted_input, user_timedelta)
    result = TardisService.format_to_string(result)
    return JSONResponse({"result": result}, status_code=200)