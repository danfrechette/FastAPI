from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import percent_rank
from app import models, schemas, utils
from app.database import get_db

router = APIRouter(
    tags = ['Users'],
    prefix="/users"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #hash the Password
    hashed_password = utils.hash( user.password )
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db) ):
    user = db.query(models.User).filter( models.User.id == str(id) ).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User: {id} was not found.")
    return user