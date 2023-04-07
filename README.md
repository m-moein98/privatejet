## Description

This is a python backend framework for building REST applications. It is built on top of the ASGI specification and uses the uvicorn server.
## Installation

```bash
python setup.py bdist_wheel
pip install dist/privatejet-0.0.1-py3-none-any.whl
```

## Usage

```python
from privatejet.main import PrivateJet
from privatejet.router import JetRouter

private_jet = PrivateJet()


async def app(scope, receive, send):
    await private_jet.add_router(
        router={"prefix": "/users", "router": UserRouter}
    )
    await private_jet.start(scope=scope, receive=receive, send=send)


class UserRouter(JetRouter):
    async def get(self, request):
        await self.send_message(
            [
                {"name": "alex", "age": 20},
                {"name": "john", "age": 30},
            ]
        )

    async def get_one(self, request):
        await self.send_message({"name": "alex", "age": 20})

    async def post(self, request):
        await self.send_message(
            {
                "message": "User created successfully",
                "user": {"name": request["body"]["name"], "age": request["body"]["age"]},
            }
        )

    async def put(self, request):
        await self.send_message(
            {
                "message": "User updated successfully",
                "user": {"name": request["body"]["name"], "age": request["body"]["age"]},
            }
        )

    async def patch(self, request):
        await self.send_message(
            {
                "message": "User patched successfully",
                "user": {"name": request["body"]["name"], "age": request["body"]["age"]},
            }
        )

    async def delete(self, request):
        await self.send_message(
            {
                "message": "User deleted successfully",
            }
        )

```

## License

This project is licensed under the terms of the MIT license.