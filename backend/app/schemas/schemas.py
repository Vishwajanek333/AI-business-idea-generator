from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Idea Schemas
class IdeaBase(BaseModel):
    title: str
    description: Optional[str] = None
    business_model: Optional[str] = None
    target_audience: Optional[str] = None
    swot_analysis: Optional[str] = None
    market_potential: Optional[str] = None
    industry: Optional[str] = None
    keywords: Optional[str] = None

class IdeaCreate(IdeaBase):
    pass

class Idea(IdeaBase):
    id: int
    user_id: int
    is_favorite: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Generation Request
class GenerationRequest(BaseModel):
    keywords: str
    industry: str
    num_ideas: int = 1

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
