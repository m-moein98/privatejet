## Description

This is a python backend framework for building REST applications. It is built on top of the ASGI specification and uses the uvicorn server.
## Installation

```bash
poetry install
poetry shell
python setup.py bdist_wheel
pip install dist/privatejet-0.0.3-py3-none-any.whl
```

## Usage

```python
"""
This is an example of how to use PrivateJet.
"""
from typing import Callable

from privatejet.main import PrivateJet
from privatejet.middlewares import CORSMiddleware
from privatejet.router import JetRouter


private_jet = PrivateJet()


async def app(scope: dict[str, str], receive: Callable, send: Callable) -> None:
    """
    This function is called by the ASGI server.
    """
    await private_jet.add_middleware(CORSMiddleware)
    await private_jet.add_router(router={"prefix": "/users", "router": UserRouter})
    await private_jet.start(scope=scope, receive=receive, send=send)


class UserRouter(JetRouter):
    """
    User Router
    """

    async def get(self, request: dict[str]) -> None:
        """
        When request method is GET and the path is like this:
            - /users
        """
        await self.send_message(
            [
                {"name": "alex", "age": 20},
                {"name": "john", "age": 30},
            ]
        )

    async def get_one(self, request: dict[str]) -> None:
        """
        When request method is GET and the path is like this:
            - /users/1
        """
        await self.send_message({"name": "alex", "age": 20})

    async def post(self, request: dict[str]) -> None:
        """
        When request method is POST and the path is like this:
            - /users
        """
        await self.send_message(
            {
                "message": "User created successfully",
                "user": {
                    "name": request["body"]["name"],
                    "age": request["body"]["age"],
                },
            }
        )

    async def put(self, request: dict[str]) -> None:
        """
        When request method is PUT and the path is like this:
            - /users/1
        """
        await self.send_message(
            {
                "message": "User updated successfully",
                "user": {
                    "name": request["body"]["name"],
                    "age": request["body"]["age"],
                },
            }
        )

    async def patch(self, request: dict[str]) -> None:
        """
        When request method is PATCH and the path is like this:
            - /users/1
        """
        await self.send_message(
            {
                "message": "User patched successfully",
                "user": {
                    "name": request["body"]["name"],
                    "age": request["body"]["age"],
                },
            }
        )

    async def delete(self, request: dict[str]) -> None:
        """
        When request method is DELETE and the path is like this:
            - /users/1
        """
        await self.send_message(
            {
                "message": "User deleted successfully",
            }
        )

```

## License

This project is licensed under the terms of the MIT license.