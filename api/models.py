import re
from typing import Optional
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, constr, field_validator


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
  class Config:


    orm_mode = True


class ShowUser(TunedModel):
  user_id: uuid.UUID
  name: str 
  surname: str
  email: EmailStr
  is_active: bool


class UserCreate(BaseModel):
  name: str
  surname: str
  email: EmailStr
  password: str

  @field_validator("name")
  def validate_name(cls, value):
    if not LETTER_MATCH_PATTERN.match(value):
      raise HTTPException(status_code=422, detail="Name should contains only letters")
    return value
  
  @field_validator("surname")
  def validate_surname(cls, value):
    if not LETTER_MATCH_PATTERN.match(value):
      raise HTTPException(status_code=422, detail="Surname should contains only letters")
    return value


class DeleteUserResponse(BaseModel):
  deleted_user_id: uuid.UUID


class UpdatedUserResponse(BaseModel):
  updated_user_id: uuid.UUID


class UpdateUserRequest(BaseModel):
  name: Optional[constr(min_length=1)]
  surname: Optional[constr(min_length=1)]
  email: Optional[EmailStr]

  @field_validator('name')
  def validator_name(cls, value):
    if not LETTER_MATCH_PATTERN.match(value):
      raise HTTPException(
        status_code=422, detail='Name should contains only letters'
      )
    return value

  @field_validator("surname")
  def validate_surname(cls, value):
      if not LETTER_MATCH_PATTERN.match(value):
          raise HTTPException(
              status_code=422, detail="Surname should contains only letters"
          )
      return value
  

class Token(BaseModel):
     access_token: str
     token_type: str