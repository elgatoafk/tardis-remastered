import secrets
import pytz
from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.src.util.models import TimeZone, InviteCode


def generate_invite_code(owner_id: int, db: Session) -> InviteCode:
    """
    Generate a random invite code for user registration.

    This function creates a unique invite code using a secure random generator.
    The invite code is associated with the owner who generated it and is stored
    in the database for later validation during user registration.

    Args:
        owner_id (int): The ID of the user (owner) generating the invite code.
        db (Session): The SQLAlchemy database session used to interact with the database.

    Returns:
        InviteCode: The newly created InviteCode object containing the generated code.
    """
    code = secrets.token_urlsafe(16)
    invite_code = InviteCode(code=code, created_by=owner_id)
    db.add(invite_code)
    db.commit()
    db.refresh(invite_code)
    return invite_code


def create_timezone(name: str, db: Session):
    """
    Validate and create a new timezone in the database.

    This function checks if the provided timezone name is valid according to the
    IANA timezones using the `pytz` library. If the timezone is valid and doesn't
    already exist in the database, it creates a new entry for it.

    Args:
        name (str): The name of the timezone to be added. Must be a valid IANA timezone.
        db (Session): The SQLAlchemy database session used to interact with the database.

    Raises:
        HTTPException: If the provided timezone name is not valid or already exists in the database.

    Returns:
        TimeZone: The newly created TimeZone object.
    """
    if name not in pytz.all_timezones:
        raise HTTPException(status_code=400, detail="Invalid timezone")

    existing_timezone = db.query(TimeZone).filter(TimeZone.name == name).first()
    if existing_timezone:
        raise HTTPException(status_code=400, detail="Timezone already exists")

    new_timezone = TimeZone(name=name)
    db.add(new_timezone)
    db.commit()
    db.refresh(new_timezone)

    return new_timezone
