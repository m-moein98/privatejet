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


class UserRouter(JetRouter):
    async def get_users(self):
        await self.send_message(
            [
                {"name": "alex", "age": 20},
                {"name": "john", "age": 30},
            ]
        )

    async def handler(self, route):
        if route == "/":
            await self.get_users()


async def app(scope, receive, send):
    private_jet = PrivateJet()
    await private_jet.add_router(
        router={"prefix": "/users", "send": send, "router": UserRouter}
    )
    await private_jet.start(scope=scope, send=send)

```

## License

This project is licensed under the terms of the MIT license.