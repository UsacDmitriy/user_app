from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
from app.exceptions import UserNoTFound

logger = logging.getLogger(__name__)


def add_exception_handler(app: FastAPI) -> None:
    @app.exception_handler(UserNoTFound)
    async def handle_user_not_exception(request: Request, exc: UserNoTFound):
        logger.error(f"Non-existed user {exc.user_id} was requested")
        return JSONResponse(status_code=404, content="User does not exist")

    return None
