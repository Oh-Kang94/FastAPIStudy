from pydantic import BaseModel


class GetProducts(BaseModel):
    class Response(BaseModel):
        id: int
        name: str