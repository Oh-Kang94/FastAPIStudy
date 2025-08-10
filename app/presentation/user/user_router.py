from fastapi import APIRouter

from app.presentation.common.api_tags import ApiTags
from app.presentation.common.common_response import CommonResponse
from app.presentation.user.dto.sign_in import SignIn
from app.presentation.user.dto.sign_up import SignUp

user_router = APIRouter(prefix="/user", tags=[ApiTags.USER])


@user_router.post("/sign-up", name="회원 가입")
async def sign_up(_user: SignUp.Request) -> CommonResponse[None]:
    return CommonResponse()


@user_router.post("/sign-in", name="로그인")
async def sign_in(_user: SignIn.Request) -> CommonResponse[None]:
    return CommonResponse()
