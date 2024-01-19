"""
Middlewares for PrivateJet
"""

from typing import Callable


class CORSMiddleware:
    """
    Middleware for CORS
    """

    async def __call__(
        self, scope: dict[str, str], receive: Callable, send: Callable
    ) -> None:
        """
        This middleware adds the CORS headers to the response.
        """
        if scope["method"] != "OPTIONS":
            return None
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"access-control-allow-origin", b"null"],
                    [
                        b"access-control-allow-headers",
                        b"access-control-allow-methods,access-control-allow-origin",
                    ],
                ],
            }
        )
        await send({"type": "http.response.body", "body": b"", "more_body": False})
