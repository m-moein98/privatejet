Router
======================================
JetRouter
--------------------------------------
The class **JetRouter** is the custom router class that will handle our **requests**. We are using the **ASGI** specification for our router class.

How to use
--------------------------------------

::

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