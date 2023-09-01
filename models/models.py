from pydantic import BaseModel


class Doc(BaseModel):
    imsi: str
    description: str | None = None
    price: float | None = None
    tax: float | None = None
    schema_version: int | None = None
    msisdn: list | None = None
    imeisv: list | None = None
    mme_host: list | None = None
    mme_realm: list | None = None
    purge_flag: list | None = None
    security: dict | None = None
    ambr: dict | None = None
    slice: list | None = None
    access_restriction_data: int | None = None
    subscriber_status: int | None = None
    network_access_mode: int | None = None
    subscribed_rau_tau_timer: int | None = None
    # __v: int | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [

                {
                    "imsi": "123456789",
                    "msisdn": [
                        "54654324",
                        "4485499494"
                    ],
                    "imeisv": [],
                    "mme_host": [],
                    "mme_realm": [],
                    "purge_flag": [],
                    "security": {
                        "k": "465B5CE8 B199B49F AA5F0A2E E238A6BC",
                        "op": None,  # when not using
                        "opc": "E8ED289D EBA952E4 283B54E8 8E6183CA",
                        "amf": "8000"
                    },
                    "ambr": {
                        "downlink": {
                            "value": 1,
                            "unit": 3
                        },
                        "uplink": {
                            "value": 1,
                            "unit": 3
                        }
                    },
                    "slice": [
                        {
                            "sst": 1,
                            "default_indicator": True,
                            "session": [
                                {
                                    "name": "internet",
                                    "type": 3,
                                    "qos": {
                                        "index": 9,
                                        "arp": {
                                            "priority_level": 8,
                                            "pre_emption_capability": 1,
                                            "pre_emption_vulnerability": 1
                                        }
                                    },
                                    "ambr": {
                                        "downlink": {
                                            "value": 1,
                                            "unit": 0#bps
                                        },
                                        "uplink": {
                                            "value": 1,
                                            "unit": 4#tbps
                                        }
                                    },

                                    "pcc_rule": []
                                }
                            ],

                        }
                    ],
                    "access_restriction_data": 32,
                    "subscriber_status": 0,
                    "network_access_mode": 0,
                    "subscribed_rau_tau_timer": 12,

                }

            ]
        }
    }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    company: str
    full_name: str | None = None
    disabled: bool | None = None
    hashed_password: str


class UserInDB(User):
    hashed_password: str
