from fastapi import FastAPI
from fastapi.routing import APIRouter
from api.handlers import user_router

import uvicorn





app = FastAPI(title="Unuversity")

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(main_api_router)

if __name__ == '__main__':
  uvicorn.run(app, host='localhost', port=8000)
