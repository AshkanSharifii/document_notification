from pydantic import BaseModel, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber


# ---------------------------------------------------------------------------
class SendOTPDTO(BaseModel):
    """Data Transfer Object for sending OTP requests.

    Validates and cleans phone numbers and OTP codes for SMS sending.
    """

    phone_number: PhoneNumber
    otp: str = Field(max_length=4)

    @field_validator("phone_number", mode="after")
    def clean_phone_number(cls, value: PhoneNumber) -> str:
        cleaned = str(value).replace("-", "")
        cleaned = cleaned.replace("+98", "")
        return cleaned

    model_config = {
        "json_schema_extra": {
            "example": {
                "phone_number": "+989170001122",
                "otp": "1234",
            }
        }
    }
