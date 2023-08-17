from typing import Annotated
from manager.handler import Reqmanager
from fastapi import FastAPI, Header
from dotenv import dotenv_values
import logging
from constants.info_message import InfoMessage
from models.models import Doc
tags_metadata = [
    {
        "name": "mon",
        "description": "With this endpoint you can POST/PUT/GET/DELETE documents in mongoDB.",
    },
    {
        "name": "auth",
        "description": "This endpoint handle the authentication of users.",

    },
]
app = FastAPI(openapi_tags=tags_metadata)

config = dotenv_values(".env")
logger = logging.getLogger(__name__)


@app.get("/mon/", tags=["mon"])
def get_crud(imsi: Annotated[str | None, Header(description="imsi")] = None,
             username: Annotated[str | None, Header(description="username")] = None):
    condition = {'imsi': imsi}
    parts = username.split("_")
    condition['pna'] = parts[1]
    logger.info(InfoMessage.GET_REQUEST.format(parts[0]))

    mg = Reqmanager()
    res = mg.find(condition)
    return res.generate_response()

# @app.post("/mon/", tags=["mon"])
# def get_crud(doc: Doc,
#              username: Annotated[str | None, Header(description="username")] = None):
#     parts = username.split("_")
#     condition['pna'] = parts[1]
#     logger.info(InfoMessage.GET_REQUEST.format(parts[0]))
#
#     mg = Reqmanager()
#     res = mg.find(condition)
#     return res.generate_response()