import time

from faststream.rabbit import RabbitRouter

from run.exec_service import execute_with_limits
from run.models import TaskRunSubscriberRequest, TaskRunCacheRequest
from run.cache import send_run_task

router = RabbitRouter()

@router.subscriber("task-run-task")
async def run_task(task: TaskRunSubscriberRequest) -> None:
    start = time.time()
    res = execute_with_limits(code=task.code, timeout=task.time_limit).strip()
    time_completed = round(float(time.time() - start), 2)
    if res == task.answer:
        result = TaskRunCacheRequest(
            uuid=task.uuid,
            res=True,
            completed_time=time_completed,
        )
    else:
        result = TaskRunCacheRequest(
            uuid=task.uuid,
            res=False,
            completed_time=time_completed,
        )

    await send_run_task(task=result)

