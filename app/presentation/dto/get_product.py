from pydantic import BaseModel


class GetProducts(BaseModel):
    class Response(BaseModel):
        id: str
        name: str