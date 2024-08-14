from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from backend.src.util.db import get_db
from backend.src.util.utility import create_timezone

router = APIRouter()


@router.post("/timezones/")
def add_timezone(timezone_name: str, db: Session = Depends(get_db)):
    """
    Add a new timezone to the database.

    This route handles the creation of a new timezone entry in the database. The provided
    timezone name is first validated against IANA timezones. If the timezone is valid
    and does not already exist, it is added to the database. If an error occurs during
    the process, an appropriate HTTP exception is raised.

    Args:
        timezone_name (str): The name of the timezone to be added. Must be a valid IANA timezone.
        db (Session): The SQLAlchemy database session used to interact with the database.

    Raises:
        HTTPException: If the provided timezone name is invalid or already exists in the database.

    Returns:
        JSONResponse: A JSON response containing a success message and the name of the newly added timezone.
                      The response status code is 200 upon successful creation.
    """
    try:
        timezone = create_timezone(timezone_name, db)
    except HTTPException as http_exc:
        raise http_exc
    return JSONResponse({"message": "Timezone added successfully", "timezone": timezone.name}, status_code=200)
