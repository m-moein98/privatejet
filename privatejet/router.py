import json


class JetRouter:
    def __init__(self, send):
        self.send = send

    async def send_message(self, message: str):
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

    async def not_found(self):
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

    async def unsupported_method(self):
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

    async def middleware_error(self):
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
        await self.send(
            {
                "type": "http.response.body",
                "body": b"Middleware Error"
            }
        )
