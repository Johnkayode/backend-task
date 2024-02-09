from aioredis import create_redis_pool
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


async def load_cache():
    redis = await create_redis_pool('redis://redis')
    FastAPICache.init(
        RedisBackend(redis), 
        prefix="fastapi-cache"
    )