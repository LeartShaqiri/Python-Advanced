from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY_NAME = "api_key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Depends(api_key_header)):
    allowed_api_key = os.getenv("API_KEY", "").split(",")

    print("Allowed API Keys:", api_key)
    print("Received API Key:", api_key)


    if api_key not in allowed_api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate API key",
        )
    print("API Key is valid")
    return api_key

      