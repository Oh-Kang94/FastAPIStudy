from fastapi import APIRouter, Depends, Path, Query, status
from sqlmodel import Session

from app.application.product_service import ProductService
from app.config.db_config import get_session
from app.presentation.common.api_tags import ApiTags
from app.presentation.common.common_response import (
    CommonResponse,
    NotFoundResourceException,
)
from app.presentation.product.dto.add_product import AddProduct
from app.presentation.product.dto.get_product import GetProducts

product_router = APIRouter(prefix="/product", tags=[ApiTags.PRODUCT])


# Service 의존성 주입
def get_product_service(session: Session = Depends(get_session)):
    return ProductService(session)


@product_router.post("", status_code=status.HTTP_201_CREATED)
async def add_product(
    product: AddProduct.Request,
    service: ProductService = Depends(get_product_service),
) -> CommonResponse[None]:
    service.create_product(
        name=product.name,
        price=100,
        stock=1000,
    )
    return CommonResponse()


@product_router.get("", response_model=CommonResponse[list[GetProducts.Response]])
async def get_product_list(
    service: ProductService = Depends(get_product_service),
) -> CommonResponse[list[GetProducts.Response]]:
    products = service.get_products()
    # DTO 변환
    res_data = [GetProducts.Response.from_entity(p) for p in products]
    return CommonResponse(data=res_data)


@product_router.get("/path/{product_id}")
async def get_product_by_parameter(
    product_id: int = Path(
        ..., title="The ID of the product to retrieve", example=1, ge=1
    ),
    service: ProductService = Depends(get_product_service),
) -> CommonResponse[GetProducts.Response]:
    product = service.get_product(product_id)
    if not product:
        raise NotFoundResourceException(id=product_id)
    return CommonResponse(data=GetProducts.Response.from_entity(product))


@product_router.get(
    "/query",
    responses={
        404: {"description": "Not Found"},
        422: {"description": "ValidationError"},
    },
)
async def get_product_by_query(
    product_id: int = Query(None, ge=1),
    service: ProductService = Depends(get_product_service),
) -> CommonResponse[GetProducts.Response | None]:
    if product_id is None:
        return CommonResponse(data=None)

    product = service.get_product(product_id)
    if not product:
        raise NotFoundResourceException(id=product_id)
    return CommonResponse(data=GetProducts.Response.from_entity(product))
