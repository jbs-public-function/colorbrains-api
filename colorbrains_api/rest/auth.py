import os

from fastapi import HTTPException
from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

from starlette import status
from starlette.requests import Request


API_KEY = os.environ["X_API_KEY"]
API_KEY_NAME = "x-api-key"

api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
    request: Request,
    api_key_header: str = Security(api_key_header_auth)
):
    # @todo - write out code for key validation
    return
