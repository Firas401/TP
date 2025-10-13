from pydantic import BaseModel, EmailStr, ValidationError, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, v):
        if v <= 0:
            raise ValueError(f"account_id must be positive: {v}")
        return v
