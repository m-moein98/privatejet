Getting Started!
======================================

Installation
--------------------------------------
Using ``pip``:
   .. code-block:: bash
      :name: Download and install PrivateJet

      $ pip install privatejet

.. seealso::
   You can also check out the `PyPI
   <https://pypi.org/project/privatejet/>`_.


Quickstart
--------------------------------------
Create a file ``main.py`` with::

   from privatejet.main import PrivateJet
   from privatejet.router import JetRouter

   private_jet = PrivateJet()

   async def app(scope, receive, send):
      await private_jet.add_router(
         router={"prefix": "/users", "router": UserRouter}
      )
      await private_jet.start(scope=scope, receive=receive, send=send)

   class UserRouter(JetRouter):
      async def get(self, request):
         await self.send_message(
               [
                  {"name": "alex", "age": 20},
                  {"name": "john", "age": 30},
               ]
         )


Run the server with::

   $ uvicorn main:app --reload

.. note::
   * ``main``: the file ``main.py``.
   * ``app``: is the name of the variable.
   * ``--reload`` flag will make the server reload on code changes.

Check it:
    Open your browser at http://127.0.0.1:8000/users

You will see the JSON response as::

    [{"name": "alex", "age": 20}, {"name": "john", "age": 30}]