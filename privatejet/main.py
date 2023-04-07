import json


class PrivateJet:
    routers = []

    async def read_body(self, receive):
        """
        Read and return the entire body from an incoming ASGI message.
        """
        body = b''
        more_body = True

        while more_body:
            message = await receive()
            body += message.get('body', b'')
            more_body = message.get('more_body', False)

        return json.loads(body)

    async def start(self, receive, scope, send):
        self.scope = scope
        assert scope["type"] == "http"
        route = scope["path"]
        for router in self.routers:
            if str(route).startswith(router["prefix"]):
                request = {
                    "method": scope["method"],
                    "path": scope["path"],
                    "query_string": scope["query_string"],
                    "headers": scope["headers"],
                }
                if request["method"] in ["POST", "PUT", "PATCH"]:
                    request["body"] = await self.read_body(receive)
                match scope["method"]:
                    case "GET":
                        if route == router["prefix"] or route == router["prefix"] + "/":
                            await router["router"](send).get(request)
                        else:
                            await router["router"](send).get_one(request)
                    case "POST":
                        await router["router"](send).post(request)
                    case "PUT":
                        await router["router"](send).put(request)
                    case "PATCH":
                        await router["router"](send).patch(request)
                    case "DELETE":
                        await router["router"](send).delete(request)

    async def add_router(self, router):
        if router["prefix"] not in [
            router_obj["prefix"] for router_obj in self.routers
        ]:
            self.routers.append(
                {
                    "prefix": router["prefix"],
                    "router": router["router"]
                }
            )
