from pydantic import BaseModel

from app.presentation.product.dto.get_product import GetProducts


class AddProduct(BaseModel):
    class Request(BaseModel):
        id: int
        name: str

        def parse_res(self) -> GetProducts.Response:
            return GetProducts.Response(id=self.id, name=self.name)
