import secrets
from sqlalchemy.orm import Session
from backend.src.util.models import InviteCode


def generate_invite_code(owner_id: int, db: Session) -> InviteCode:
    """Generates a random invite code for user registration"""
    code = secrets.token_urlsafe(16)
    invite_code = InviteCode(code=code, created_by=owner_id)
    db.add(invite_code)
    db.commit()
    db.refresh(invite_code)
    return invite_code
