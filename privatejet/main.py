class PrivateJet:
    routers = []

    async def start(self, scope, send):
        self.scope = scope
        self.send = send
        assert scope["type"] == "http"
        route = scope["path"]
        for router in self.routers:
            if str(route).startswith(router["prefix"]):
                router_class = router["router"](send=send)
                await router_class.handler(route=route[router["prefix"].__len__() :])

    async def add_router(self, router):
        if router["prefix"] not in [
            router_obj["prefix"] for router_obj in self.routers
        ]:
            self.routers.append(router)
