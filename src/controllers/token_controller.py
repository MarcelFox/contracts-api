from datetime import datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from src.repositories.tenant_repository import TenantRepository
from src.schema.tenant_schema import TenantSchema
from src.shared.controller_class import Controller

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    tenant: str
    exp: datetime
    iat: datetime


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    tenant: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


class TokenController(Controller):
    def __init__(self):
        super().__init__()

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        to_encode.update({"iat": datetime.utcnow()})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def decode_token(self, token: str) -> Token | None:
        print(f"will decode token: {token}")
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            print(f"Decoded token: {payload}")
            return payload
        except jwt.PyJWTError as err:
            print(f"Cannot decode token: {err}")
            return None

    async def get_tenant(self, tenant_id: str) -> TenantSchema:
        found_tenant = await TenantRepository().find({"tenant_id": tenant_id})
        if not found_tenant:
            raise ValueError("Tenant not found")
        return found_tenant

    def fake_hash_password(self, password: str):
        return "fakehashed" + password

    def get_user(self, db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)

    async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
        decoded_token = TokenController().decode_token(token)
        if decoded_token:
            tenant = decoded_token["tenant"]
            print(f"Tenant {tenant}")
            found_tenant = await TokenController().get_tenant(tenant)
            if not found_tenant:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return found_tenant
        return None

    async def get_current_active_user(
        self,
        current_user: Annotated[User, Depends(get_current_user)],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
