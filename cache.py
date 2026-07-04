import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.from_url(REDIS_URL, decode_responses=True)

def get_cached_url(code):
    result =r.get(code)
    if result is None:
        return None
    return result

def set_cached_url(code,original_url):
    r.set(code,original_url,ex=3600)

