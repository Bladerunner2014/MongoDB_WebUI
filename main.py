from typing import Annotated
from manager.handler import Reqmanager
from fastapi import FastAPI, Header, Body, status
from dotenv import dotenv_values
import logging
from constants.info_message import InfoMessage
from models.models import Doc
from log import log
from http_handler.response_handler import ResponseHandler

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
    # condition['pna'] = parts[1]

    logger.info(InfoMessage.GET_REQUEST.format(username=username, imsi=imsi))

    mg = Reqmanager()
    res = mg.find(condition)
    return res.generate_response()


@app.post("/mon/", tags=["mon"], response_model=dict)
def post_crud(doc: Annotated[Doc | None, Body(description="Document")] = None,
              username: Annotated[str | None, Header(description="username")] = None):
    # parts = username.split("_")
    res = ResponseHandler()

    # condition['pna'] = parts[1]
    logger.info(InfoMessage.POST_REQUEST.format(username=username, document=doc))
    mg = Reqmanager()
    res = mg.insert(dict(doc))
    return res.generate_response()


@app.put("/mon/", tags=["mon"],response_model=dict)
def put_crud(doc: Annotated[Doc | None, Body(description="Document")] = None,
             username: Annotated[str | None, Header(description="username")] = None):
    # parts = username.split("_")
    res = ResponseHandler()

    # condition['pna'] = parts[1]
    logger.info(InfoMessage.PUT_REQUEST.format(username=username, document=doc))
    mg = Reqmanager()
    res = mg.update(dict(doc))
    return res.generate_response()


@app.delete("/mon/", tags=["mon"], response_model=dict)
def delete_crud(imsi: Annotated[str | None, Header(description="imsi")] = None,
                username: Annotated[str | None, Header(description="username")] = None):
    # parts = username.split("_")
    res = ResponseHandler()
    condition = {"imsi": imsi}
    # condition['pna'] = parts[1]
    logger.info(InfoMessage.DELETE_REQUEST.format(username=username, document=imsi))
    mg = Reqmanager()
    res = mg.delete(condition)
    return res.generate_response()


log.setup_logger()
