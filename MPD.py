from fastapi import APIRouter, Request, HTTPException
import requests

router = APIRouter()

@router.get("/mpd")
def get_mpd(request: Request, password: str):
    if password != request.app.api_password:
        raise HTTPException(status_code=403, detail="Forbidden")

    url = "https://raw.githubusercontent.com/nzo66/TV/refs/heads/main/mpd.m3u" 
    return response.text
