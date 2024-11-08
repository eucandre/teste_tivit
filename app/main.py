from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import TokenRequest
from app.auth import login_for_access_token
from app.database import SessionLocal
from app.models import User
from app.auth import get_user_role_user, get_user_role_admin

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/token")
def login_for_access_token_endpoint(form_data: TokenRequest, db: Session = Depends(get_db)):
    return login_for_access_token(form_data=form_data, db=db)


@app.get("/user")
def get_user_role_user(db: Session = Depends(get_db)):
    return {"message": "Acesso permitido para o papel user"}


@app.get("/admin")
def get_user_role_admin(db: Session = Depends(get_db)):
    return {"message": "Acesso permitido para o papel admin"}
