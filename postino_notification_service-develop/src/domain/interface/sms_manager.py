from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
class ISmsManager(ABC):
    """Abstract base class for SMS manager implementations.

    Defines the interface for sending OTP SMS messages.
    """

    @abstractmethod
    def send_otp_sms(self, otp: str, mobile: str) -> dict: ...
