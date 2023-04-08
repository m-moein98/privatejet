class CORSMiddleware:
    async def __call__(self, scope, receive, send):
        if scope["method"] == "OPTIONS":
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        [b"access-control-allow-origin", b"null"],
                        [
                            b"access-control-allow-headers",
                            b"access-control-allow-headers,access-control-allow-methods,access-control-allow-origin"
                        ],
                    ],
                }
            )
            await send({"type": "http.response.body", "body": b"", "more_body": False})
