from fastapi import APIRouter

from app.presentation.common.common_response import CommonResponse
from app.presentation.dto.add_product import AddProduct
from app.presentation.dto.get_product import GetProducts


product_router = APIRouter(prefix="/product")

product_list : list[GetProducts.Response] = []


@product_router.post("")
async def addProduct(product: AddProduct.Request) -> CommonResponse[None]:
    product_list.append(product.parse_res())
    return CommonResponse()


@product_router.get("")
async def getProductList() -> CommonResponse[list[GetProducts.Response]]:
    return CommonResponse(data=product_list)
