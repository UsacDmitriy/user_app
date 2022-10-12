from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes.user import create_user_router
from app.exception_handler import add_exception_handler


def create_application() -> FastAPI:
    user_router = create_user_router()
    app = FastAPI()
    app.include_router(user_router)
    add_exception_handler(app)

    return app


app = create_application()
