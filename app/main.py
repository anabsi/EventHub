from fastapi import FastAPI
from endpoints import router

app = FastAPI(title="Event Hub API")
app.include_router(router)
