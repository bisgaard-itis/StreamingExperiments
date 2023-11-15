

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from typing import AsyncIterable
import asyncio

app = FastAPI()


async def _generator() -> AsyncIterable[str]:
    for ii in range(100):
        yield f"#iteration: {ii}\n"
        await asyncio.sleep(2)
    


@app.get("/")
async def root() -> StreamingResponse:
    return StreamingResponse(_generator())