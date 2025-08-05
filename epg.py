from fastapi import APIRouter, Request, HTTPException
import requests

router = APIRouter()

@router.get("/epg")
def get_epg(request: Request, password: str):
    if password != request.app.api_password:
        raise HTTPException(status_code=403, detail="Forbidden")

    url = "https://raw.githubusercontent.com/nzo66/TV/refs/heads/main/epg.xml"  
    response = requests.get(url)
    return response.text
