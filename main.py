import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.api.api_v1.api import router as api_router
from app.core.config import API_V1_STR, PROJECT_NAME


app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod/api"
)


app.include_router(api_router, prefix=API_V1_STR)


@app.get("/ping")
def pong():
    return {"ping": "pong!"}

# @app.on_event("startup")
# async def startup():
#     await db.database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await db.database.disconnect()

handler = Mangum(app, enable_lifespan=False)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

