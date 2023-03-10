from typing import Optional
import uuid
from pydantic import BaseModel, Field

class TaskModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    completed: bool = False
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "My important task",
                "completed": True,
            }
        }
        
class UpdateTaskModel(BaseModel):
    name: Optional[str]
    completed: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "name": "My important task",
                "completed": True,
            }
        }
            