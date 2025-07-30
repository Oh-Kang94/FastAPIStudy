from fastapi import APIRouter


product_router = APIRouter(prefix="/product")

product_list = []


@product_router.post("")
async def addProduct(product: dict) -> dict[str, str]:
    product_list.append(product)
    return {
        "msg": "Product Add Successfully"
    }


@product_router.get("")
async def getProductList() -> list[dict[str, str]]:
    return product_list
