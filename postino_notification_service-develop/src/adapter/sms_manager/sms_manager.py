import httpx

from src.config import settings
from src.domain.interface.sms_manager import ISmsManager


# ---------------------------------------------------------------------------
class SmsManager(ISmsManager):
    """SMS manager implementation for sending OTP messages via SMS.ir API.

    Attributes:
        __base_url (str): The base URL for the SMS.ir API.
        __api_key (str): The API key for authenticating with SMS.ir.
    """

    def __init__(self):
        self.__base_url = "https://api.sms.ir/"
        self.__api_key = settings.SMS_PROVIDER_API_KEY

    async def send_otp_sms(self, otp: str, mobile: str) -> dict:
        payload = {
            "mobile": mobile,
            "templateId": settings.SMS_PROVIDER_OTP_TEMPLATE_ID,
            "parameters": [{"name": "code", "value": otp}],
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "text/plain",
            "x-api-key": self.__api_key,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.__base_url + "v1/send/verify", json=payload, headers=headers
            )

        response_data = response.json()

        if response_data.get("status") == 1:
            return {"success": True, "message": response_data.get("message")}

        return {"success": False, "message": response_data.get("message")}
