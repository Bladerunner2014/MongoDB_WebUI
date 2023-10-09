from typing import Annotated
from manager.handler import Reqmanager
from fastapi import FastAPI, Body
import logging
from constants.info_message import InfoMessage
from models.models import Token, User, model_config
from log import log
from security.details import *
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware

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
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
config = dotenv_values(".env")
logger = logging.getLogger(__name__)


@app.get("/mon/{imsi}", tags=["mon"])
def get_crud(imsi, current_user: Annotated[User, Depends(get_current_active_user)] = None,
             ):
    condition = {'imsi': imsi, 'slice.session.name': current_user.company}

    logger.info(InfoMessage.GET_REQUEST.format(username=current_user.username, imsi=imsi))

    mg = Reqmanager()
    res = mg.find(condition)
    return res.generate_response()


@app.post("/mon/", tags=["mon"], response_model=dict)
def post_crud(current_user: Annotated[User, Depends(get_current_active_user)] = None,
              doc: Annotated[dict | None, Body(examples=[model_config], description="Document")] = None):
    logger.info(InfoMessage.POST_REQUEST.format(username=current_user.username, document=doc))
    mg = Reqmanager()
    res = mg.insert(dict(doc))
    return res.generate_response()


@app.post("/mon/batch", tags=["mon"])
def post_crud(
              batch):
    # logger.info(InfoMessage.POST_REQUEST.format(username=current_user.username, document="xml"))
    print(batch)
    # mg = Reqmanager()
    # res = mg.insert(batch)
    # return res.generate_response()
    return 200


@app.put("/mon/", tags=["mon"], response_model=dict)
def put_crud(
        doc: Annotated[dict | None, Body(examples=[model_config], description="Document")] = None,
        current_user: Annotated[User, Depends(get_current_active_user)] = None):
    logger.info(InfoMessage.PUT_REQUEST.format(username=current_user.username, document=doc))
    mg = Reqmanager()
    res = mg.update(dict(doc))
    return res.generate_response()


@app.delete("/mon/{imsi}", tags=["mon"], response_model=dict)
def delete_crud(imsi,
                current_user: Annotated[User, Depends(get_current_active_user)] = None):
    condition = {"imsi": imsi, 'slice.session.name': current_user.company}
    logger.info(InfoMessage.DELETE_REQUEST.format(username=current_user.username, document=imsi))
    mg = Reqmanager()
    res = mg.delete(condition)
    return res.generate_response()


@app.post("/token", tags=["auth"], response_model=Token)
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
    access_token_expires = timedelta(minutes=int(config["ACCESS_TOKEN_EXPIRE_MINUTES"]))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer", "apn": user.company}


# @app.get("/users/me/", tags=["test"], response_model=User)
# async def read_users_me(
#         current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return current_user
#
#
# @app.get("/users/me/items/", tags=["test"])
# async def read_own_items(
#         current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]


log.setup_logger()
