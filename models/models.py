from pydantic import BaseModel

class Doc(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
