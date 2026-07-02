import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

def get_cached_url(code):
    result =r.get(code)
    if result is None:
        return None
    return result

def set_cached_url(code,original_url):
    r.set(code,original_url,ex=3600)

