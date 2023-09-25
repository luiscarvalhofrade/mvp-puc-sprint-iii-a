from pydantic import BaseModel
from typing import List

class OrderSchema(BaseModel):
    """ Define como um novo pedido a ser inserido deve ser representado
    """
    product_id: int = 10
    quantity: int = 12

class OrderDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    id: str

class OrderUpdateSchema(BaseModel):
    id: int
    quantity: int

class OrderViewSchema(BaseModel):
    id: int