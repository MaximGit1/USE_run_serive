import asyncio

from faststream import FastStream
from faststream.rabbit import RabbitBroker

from run.subscriber import router

async def main(app_: FastStream):
    await app_.run()


if __name__ == '__main__':
    broker = RabbitBroker()
    broker.include_router(router)
    app = FastStream(broker)

    asyncio.run(main(app))