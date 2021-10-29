from fastapi import FastAPI, Request, Response
from modelRequest import DataRequest

api = FastAPI()


@api.get("/webhook")
async def verify(request: Request):
    if request.query_params.get("hub.verify_token") == "bot-fordez":
        return Response(content=request.query_params["hub.challenge"])
    else:
        return Response(content="Se requiere un token de verificacion", status_code=400)


@api.post("/webhook")
def webhook(data: DataRequest):
    messaging = list(
        map(lambda messaging: messaging['messaging'], data.entry))
    userId = list(
        map(lambda sender: sender['sender']['id'], messaging[0]))
    pageId = list(
        map(lambda recipient: recipient['recipient']['id'], messaging[0]))
    message = list(
        map(lambda message: message['message']['text'], messaging[0]))
    print(userId[0])
    print(pageId[0])
    print(message[0])

    return Response("ok", status_code=200)
