from pydantic import BaseModel


model_config = {
    "schema_version": 1,
    "imsi": "1",
    "msisdn": [
        "Lorem"
    ],
    "imeisv": [],
    "mme_host": [],
    "mme_realm": [],
    "purge_flag": [],
    "security": {
        "k": "465B5CE8 B199B49F AA5F0A2E E238A6BC",
        "op": None,
        "opc": "E8ED289D EBA952E4 283B54E8 8E6183CA",
        "amf": "8000",
        "sqn": 2625
    },
    "ambr": {
        "downlink": {
            "value": 10,
            "unit": 3
        },
        "uplink": {
            "value": 10,
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
                            "value": 10,
                            "unit": 3
                        },
                        "uplink": {
                            "value": 10,
                            "unit": 3
                        }
                    },
                    "ue": {
                        "addr": "10.45.0.4",
                        "addr6": "Lorem"
                    },
                    "pcc_rule": [
                        {
                            "flow": [],
                            "qos": {
                                "arp": {
                                    "pre_emption_capability": 43,
                                    "pre_emption_vulnerability": -53,
                                    "priority_level": 57
                                },
                                "gbr": {
                                    "downlink": {
                                        "unit": 62,
                                        "value": -96
                                    },
                                    "uplink": {
                                        "unit": -69,
                                        "value": -40
                                    }
                                },
                                "index": 10
                            }
                        }
                    ],
                    "smf": {
                        "addr": "Lorem",
                        "addr6": "Lorem"
                    }
                }
            ],
            "sd": "Lorem"
        }
    ],
    "access_restriction_data": 32,
    "subscriber_status": 0,
    "network_access_mode": 0,
    "subscribed_rau_tau_timer": 12,
    "__v": 0
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
