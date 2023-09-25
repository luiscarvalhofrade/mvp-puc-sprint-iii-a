from pydantic import BaseModel

class ProductViewSchema(BaseModel):
    id: int