from fastapi import APIRouter, Request, HTTPException
import requests

router = APIRouter()

@router.get("/series")
def get_series(request: Request, password: str):
    if password != request.app.api_password:
        raise HTTPException(status_code=403, detail="Forbidden")

    url = "https://raw.githubusercontent.com/nzo66/TV/refs/heads/main/serie.m3u" 
    response = requests.get(url)
    return response.text
