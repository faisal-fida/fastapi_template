import re

from pydantic import EmailStr, Field, field_validator

from src.models import CustomModel



class AuthUser(CustomModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)

    @field_validator("password", mode="after")
    @classmethod
    def valid_password(cls, password: str) -> str:
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")

        return password


class JWTData(CustomModel):
    user_id: int = Field(alias="sub")
    is_admin: bool = False


class AccessTokenResponse(CustomModel):
    access_token: str
    refresh_token: str


class UserResponse(CustomModel):
    email: EmailStr
