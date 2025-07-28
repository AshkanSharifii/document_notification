from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from src.application.use_case.send_otp_use_case import SendOTPUseCase
from src.di.container import Container
from src.presentation.rest.dto.send_otp_dto import SendOTPDTO

# ---------------------------------------------------------------------------
sms_router = APIRouter()


# ---------------------------------------------------------------------------
@sms_router.post("/send/otp", status_code=status.HTTP_200_OK)
@inject
async def send_otp(
    otp_request: SendOTPDTO,
    send_otp: SendOTPUseCase = Depends(Provide[Container.send_otp_use_case]),
):
    response = await send_otp.execute(otp_request.otp, otp_request.phone_number)
    return response
