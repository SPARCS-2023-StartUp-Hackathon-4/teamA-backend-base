from datetime import timedelta, datetime

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_crud, user_schema
from domain.user.user_crud import pwd_context
from common.config import SECRET_KEY


ACCESS_TOKEN_EXPIRE_MINUTES = 60*24
SECRET_KEY = SECRET_KEY
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


router = APIRouter(
    prefix="/user"
)


@router.post("/", status_code=status.HTTP_200_OK)
def user_create(_user_create: user_schema.UserCreate,
                db: Session = Depends(get_db)):
    user_exists = bool(
        user_crud.get_existing_user(db, user_create=_user_create)
    )

    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Existing User')
    user_crud.create_user(db=db,
                          user_create=_user_create)


@router.post("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def user_delete(username: str,
                token: str = Depends(oauth2_scheme),
                db: Session = Depends(get_db)):
    current_user = get_current_user(token, db)
    if current_user.username == username:
        user_crud.delete_user(db, username)

    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Incorrect Username')


@router.post("/login", response_model=user_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    #
    user = user_crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect Username or PW',
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Make Access Token
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(
        data, SECRET_KEY, algorithm=ALGORITHM
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }


@router.get("/", response_model=user_schema.UserGet)
def get_current(token: str = Depends(oauth2_scheme),
                db: Session = Depends(get_db)):

    current_user = get_current_user(token, db)
    return current_user


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    else:
        user = user_crud.get_user(db, username=username)
        if user is None:
            raise credentials_exception
        return user
