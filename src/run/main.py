import asyncio
import os

from faststream import FastStream
from faststream.rabbit import RabbitBroker

from run.subscriber import router

async def main(app_: FastStream):
    await app_.run()


if __name__ == '__main__':
    broker = RabbitBroker(
    url=f"amqp://{os.getenv('RABBITMQ_USER', 'guest')}:{os.getenv('RABBITMQ_PASS', 'guest')}@{os.getenv('RABBITMQ_HOST', 'rabbitmq')}:{os.getenv('RABBITMQ_PORT', '5672')}/"
)
    broker.include_router(router)
    app = FastStream(broker)

    asyncio.run(main(app))