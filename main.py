from typing import Annotated
from manager.handler import Reqmanager
from fastapi import FastAPI, Header, Body
from dotenv import dotenv_values
import logging
from constants.info_message import InfoMessage
from models.models import Doc, Token, User
from log import log
from security.details import *
from http_handler.response_handler import ResponseHandler
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

ACCESS_TOKEN_EXPIRE_MINUTES = 30
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


@app.put("/mon/", tags=["mon"], response_model=dict)
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


@app.post("/token",tags=["auth"], response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/",tags=["test"], response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@app.get("/users/me/items/",tags=["test"])
async def read_own_items(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]


log.setup_logger()
