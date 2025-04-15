# @router.get("/")
# async def get_token():
#     return TokenController().create_access_token({"tenant": "d86c3676220f4775acb15b0b403869ea"})

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.controllers.token_controller import TokenController, UserInDB
from src.shared.config import fake_users_db

router = APIRouter()


@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    print(user_dict)
    if not user_dict:
        print("User not found")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = TokenController().fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        print(f"Incorrect password: {form_data.password} : {hashed_password}")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = TokenController().create_access_token({"tenant": "d86c3676220f4775acb15b0b403869ea"})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/hello")
async def hello(token: Annotated[str, Depends(TokenController().get_current_user)]) -> str:
    return "ok"
