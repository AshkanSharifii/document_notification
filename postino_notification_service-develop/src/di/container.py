from dependency_injector import containers, providers

from src.adapter.sms_manager.sms_manager import SmsManager
from src.application.use_case.send_otp_use_case import SendOTPUseCase


# ---------------------------------------------------------------------------
class Container(containers.DeclarativeContainer):
    """Dependency injection container for managing application services.

    Configures and provides dependencies for SMS-related services.
    """

    wiring_config = containers.WiringConfiguration(modules=["src.presentation.rest.sms.router"])

    sms_manager = providers.Factory(SmsManager)

    send_otp_use_case = providers.Factory(SendOTPUseCase, manager=sms_manager)
