from fastapi import APIRouter, Path, Query

from app.presentation.common.common_response import CommonResponse
from app.presentation.dto.add_product import AddProduct
from app.presentation.dto.get_product import GetProducts


product_router = APIRouter(prefix="/product")

product_list: list[GetProducts.Response] = []


@product_router.post("")
async def addProduct(product: AddProduct.Request) -> CommonResponse[None]:
    product_list.append(product.parse_res())
    return CommonResponse()


@product_router.get("")
async def getProductList() -> CommonResponse[list[GetProducts.Response]]:
    return CommonResponse(data=product_list)


@product_router.get("/{product_id}")
async def getProductByParameter(product_id: int = Path(..., title="The ID of the to retrieve", example=1, ge=0, lt=3)) -> CommonResponse[GetProducts.Response]:
    # Swagger 문서 표기 방법 이다.
    '''
        Path Parameter 사용 방법

        `@router.get("/{path_variable}")`

        `product_id: int = Path(..., title="The ID of the to retrieve")`
        : Path는 첫 인수로, None or ...을 받을 수 있다. ...이면, required 이다.
        title은 Swagger에 표기하고 싶은 값, 
        example은 예시.
        gt(greater than)
        ge(greater equal)
        lt(less than )
        le(less equal )
    '''
    for product in product_list:
        if product.id == product_id:
            return CommonResponse(data=product)
    raise
