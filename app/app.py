from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.presentation import routers
from app.presentation.common.exception_handler import CustomHTTPException, custom_http_exception_handler, general_exception_handler, validation_exception_handler

app = FastAPI(
    exception_handlers={
        CustomHTTPException: custom_http_exception_handler,
        RequestValidationError: validation_exception_handler,
        Exception: general_exception_handler,
    }
)

# router 등록
for router in routers:
    app.include_router(router)
