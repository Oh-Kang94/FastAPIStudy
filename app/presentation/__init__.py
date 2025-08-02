from .user.user_router import user_router
from .product.product_router import product_router

routers = [
    product_router,
    user_router,
]
