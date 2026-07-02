from fastapi import APIRouter,Depends,HTTPException
from fastapi.responses import  RedirectResponse
from models import URL
from schemas import URLCreate,URLResponse
from database import get_db
from sqlalchemy.orm import Session
from utils import generate_short_code
from cache import get_cached_url,set_cached_url
router = APIRouter()

@router.post("/shorten",response_model=URLResponse)
def shorten_url(request:URLCreate, db:Session=Depends(get_db)):
    checker= db.query(URL).filter(URL.original_url == str(request.original_url)).first()
    if checker:
        return checker
    code = generate_short_code()
    response = URL(original_url = str(request.original_url),short_code = code , hits = 0)
    db.add(response)
    db.commit()
    db.refresh(response)
    return response

@router.get("/{code}/stats")
def get_stats(code:str,db:Session=Depends(get_db)):
    result = db.query(URL).filter(URL.short_code == code).first()
    if result is None:
        raise HTTPException(status_code=404,detail="URL not found")
    return {
            "original_url":result.original_url,
            "short_code":result.short_code,
            "hits":result.hits,
            "created_at":result.created_at
            }

# @router.get("/{code}")
# def get_shortened_url(code:str,db:Session=Depends(get_db)):
    
#     result = db.query(URL).filter(URL.short_code==code).first()
#     if result is None:
#         raise HTTPException(status_code=404, detail="URL not found")
#     result.hits+=1
#     db.commit()
#     return RedirectResponse(url=result.original_url, status_code=301)


@router.get("/{code}")
def cached_url(code:str, db:Session=Depends(get_db)):
    cache = get_cached_url(code)
    print(f"Cache result for {code}: {cache}")  # add this
    if cache:
        return RedirectResponse(url=cache, status_code=301)
    result = db.query(URL).filter(URL.short_code==code).first()
    if result is None:
        raise HTTPException(status_code=404,detail="URL not found")
    result.hits+=1
    db.commit()
    set_cached_url(code,result.original_url)
    return RedirectResponse(url=result.original_url, status_code=301)



