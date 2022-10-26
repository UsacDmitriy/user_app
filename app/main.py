from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes.user import create_user_router
from app.exception_handler import add_exception_handler


def create_application() -> FastAPI:
    profile_infos, user_contents = create_profile_infos()
    user_router = create_user_router(profile_infos, user_contents)
    app = FastAPI()
    app.include_router(user_router)
    add_exception_handler(app)

    return app


def create_profile_infos():
    profile_infos = {
        0:
            {
                "short_description": "My bio description",
                "long_bio": "This is our long bio",
            },
    }
    user_contents = {
        0:
            {
                "name": "Malik",
                "liked_posts": [1, 2],
            },
    }
    return profile_infos, user_contents


from models import recreate_postgres_tables

recreate_postgres_tables()
app = create_application()
