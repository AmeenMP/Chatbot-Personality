from contextlib import asynccontextmanager

from fastapi import FastAPI

from db_connection import Base, engine
from Database import User


#ptb = (main())


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    # await ptb.bot.setWebhook("https://86.50.228.198")  # replace <your-webhook-url>
    # async with ptb:
    #     await ptb.start()
    #     yield
    #     await ptb.stop()


app = FastAPI(lifespan=lifespan)


# @app.post("/")
# async def process_update(request: Request):
#     req = await request.json()
#     update = Update.de_json(req, ptb.bot)
#     await ptb.process_update(update)
#     return Response(status_code=HTTPStatus.OK)
