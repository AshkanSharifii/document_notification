import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from src.di.container import Container
from src.presentation.rest.routers import router


# ---------------------------------------------------------------------------
def create_app() -> FastAPI:
    openapi_url = "/openapi.json" if os.environ.get("APP_ENV", "dev") == "dev" else ""
    app = FastAPI(
        title="Notification Service", default_response_class=ORJSONResponse, openapi_url=openapi_url
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    container = Container()
    container.init_resources()
    app.container = container

    return app
