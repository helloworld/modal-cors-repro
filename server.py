import modal
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

stub_name = "modal-cors-repro"
origins = [
    "*"
]

web_app = FastAPI()
stub = modal.Stub(stub_name)
image = modal.Image.debian_slim()


class Inp(BaseModel):
    name: str


class Out(BaseModel):
    greeting: str


@web_app.post("/")
async def hello_world(inp: Inp):
    return Out(greeting=f"Hello {inp.name}!")

web_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@stub.asgi(image=image)
def fastapi_app():
    return web_app


if __name__ == "__main__":
    stub.serve()
