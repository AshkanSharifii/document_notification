from src.domain.interface.sms_manager import ISmsManager


# ---------------------------------------------------------------------------
class SendOTPUseCase:
    """Use case for sending OTP to a phone number via SMS.

    Attributes:
        _sms_manager (ISmsManager): The SMS manager instance for sending messages.
    """

    def __init__(self, manager: ISmsManager):
        self._sms_manager = manager

    async def execute(self, otp: str, phone_number: str) -> dict:
        result = await self._sms_manager.send_otp_sms(otp, phone_number)
        return result
