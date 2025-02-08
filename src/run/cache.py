import json

import redis.asyncio as redis

from run.models import TaskRunCacheRequest

redis_client = redis.from_url("redis://redis:6379?decode_responses=True")

async def send_run_task(task: TaskRunCacheRequest) -> None:
    async with redis_client:
        await redis_client.setex(
            name=task.uuid,
            value=json.dumps(task.get_data()),
            time=60,
        )
