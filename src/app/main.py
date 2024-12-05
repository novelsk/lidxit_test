from fastapi import FastAPI

from app.api import setup_views
from app.conf import settings


def setup_app() -> FastAPI:
    api = FastAPI(
        title='Form API',
        docs_url=f'{settings.PREFIX}/docs',
        openapi_url=f'{settings.PREFIX}/openapi.json',
    )
    setup_views(api)
    return api


app = setup_app()
