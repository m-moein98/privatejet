"""
JetRouter is a class that handles the response of the request.
"""

import json
from typing import Callable


class JetRouter:
    """
    JetRouter is a class that handles the response of the request.
    """

    def __init__(self, send: Callable) -> None:
        """
        Initializes the JetRouter class.
        """
        self.send = send

    async def send_message(self, message: dict[str] | list[str | dict]) -> None:
        """
        Sends a message to the client.
        """
        await self.send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"application/json"],
                    [b"access-control-allow-origin", b"*"],
                ],
            }
        )
        await self.send(
            {
                "type": "http.response.body",
                "body": json.dumps(message).encode(),
            }
        )

    async def not_found(self) -> None:
        """
        Sends a 404 Not Found response.
        """
        await self.send(
            {
                "type": "http.response.start",
                "status": 404,
                "headers": [
                    [b"content-type", b"application/json"],
                    [b"access-control-allow-origin", b"*"],
                ],
            }
        )
        await self.send(
            {
                "type": "http.response.body",
                "body": b"Not Found",
            }
        )

    async def unsupported_method(self) -> None:
        """
        Sends a 405 Method Not Allowed response.
        """
        await self.send(
            {
                "type": "http.response.start",
                "status": 405,
                "headers": [
                    [b"content-type", b"application/json"],
                    [b"access-control-allow-origin", b"*"],
                ],
            }
        )
        await self.send(
            {
                "type": "http.response.body",
                "body": b"Method Not Allowed",
            }
        )

    async def middleware_error(self) -> None:
        """
        Sends a 500 Internal Server Error response.
        """
        await self.send(
            {
                "type": "http.response.start",
                "status": 500,
                "headers": [
                    [b"content-type", b"application/json"],
                    [b"access-control-allow-origin", b"*"],
                ],
            }
        )
        await self.send({"type": "http.response.body", "body": b"Middleware Error"})
