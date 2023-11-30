from fastapi_poe import make_app
from modal import Image, Stub, asgi_app

from typing import AsyncIterable

from fastapi_poe import PoeBot
from fastapi_poe.client import stream_request
from fastapi_poe.types import (
    PartialResponse,
    ProtocolMessage,
    QueryRequest,
    SettingsRequest,
    SettingsResponse,
)

from time import time, gmtime, strftime


class BotDefinitions(PoeBot):
    async def get_response(
        self, request: QueryRequest
    ) -> AsyncIterable[PartialResponse]:
        # add a system message
        sysmsgexists = False
        for protmsg in request.query:
            if protmsg.role == "system":
                sysmsgexists = True
        if not sysmsgexists:
            request.query.insert(0, ProtocolMessage(role="system", content=""))

        # update the system message
        servertime = strftime("%A, %B %-d, %Y %H:%M", gmtime(time()))
        request.query[0].content = f"It is {servertime} GMT."

        # make a stream request and hand back the output
        async for msg in stream_request(
            request, "GPT-3.5-Turbo-Instruct", request.access_key
        ):
            yield PartialResponse(text=msg.text)

    async def get_settings(self, setting: SettingsRequest) -> SettingsResponse:
        # give details about your bot
        return SettingsResponse(
            server_bot_dependencies={"GPT-3.5-Turbo-Instruct": 1},
            introduction_message="Hi! What can I do for you?",
        )


bot = BotDefinitions()

# Variables required by modal.com
image = Image.debian_slim().pip_install_from_requirements("requirements.txt")
stub = Stub("basicserverbot")


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    app = make_app(bot, access_key="XRsROUqjRsVNvTStZv9Km5CcCr7H8BlK")
    return app
