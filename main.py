import json
import os
import shutil
from typing import Union

import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI

from src.config import global_vars

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def load_env():
    if not os.path.exists('.env'):
        shutil.copy('.env.example', '.env')

    for key, value in (dotenv_values() | dict(os.environ)).items():
        global_vars.set_value(key, value)


def main():
    # 加载环境变量到全局配置中
    load_env()

    # 启动Uvicorn服务器
    uvicorn.run(
        "main:app",
        host=global_vars.get_value("FASTAPI_HOST"),
        port=int(global_vars.get_value("FASTAPI_PORT")),
        log_level=global_vars.get_value("LOG_LEVEL"),
        reload=global_vars.get_value("ENVIRONMENT").lower() == "dev"
    )


if __name__ == '__main__':
    main()