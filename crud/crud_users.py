import uuid
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models.user_model import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔐 HASH
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# 🔍 GETS
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

# ➕ CREATE
def create_user(db: Session, name: str, email: str, password: str):
    hashed_password = get_password_hash(password)
    user = User(
        id=str(uuid.uuid4()),
        name=name,
        email=email,
        password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# 🔐 LOGIN
def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

# ✏️ UPDATE
def update_user(db: Session, user_id: str, name: str, email: str):
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    user.name = name
    user.email = email

    db.commit()
    db.refresh(user)
    return user