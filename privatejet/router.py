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
                    [b"content-type", b"text/plain"],
                ],
            }
        )
        await self.send(
            {
                "type": "http.response.body",
                "body": json.dumps(message).encode(),
            }
        )
