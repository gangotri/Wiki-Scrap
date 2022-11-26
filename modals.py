from pydantic import BaseModel

class Scrap(BaseModel):
    title:str
    description: str