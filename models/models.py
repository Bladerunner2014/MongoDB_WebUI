from pydantic import BaseModel


class Doc(BaseModel):
    imsi: str
    description: str | None = None
    # price: float
    # tax: float | None = None

#   schema_version: int
#   msisdn: list
#   imeisv: list
#   mme_host: list,
#   "mme_realm": [],
#   "purge_flag": [],
#   "security": {
#     "k": "465B5CE8 B199B49F AA5F0A2E E238A6BC",
#     "op": null,
#     "opc": "E8ED289D EBA952E4 283B54E8 8E6183CA",
#     "amf": "8000"
#   },
#   "ambr": {
#     "downlink": {
#       "value": 1,
#       "unit": 3
#     },
#     "uplink": {
#       "value": 1,
#       "unit": 3
#     }
#   },
#   "slice": [
#     {
#       "sst": 1,
#       "default_indicator": true,
#       "session": [
#         {
#           "name": "internet",
#           "type": 3,
#           "qos": {
#             "index": 9,
#             "arp": {
#               "priority_level": 8,
#               "pre_emption_capability": 1,
#               "pre_emption_vulnerability": 1
#             }
#           },
#           "ambr": {
#             "downlink": {
#               "value": 1,
#               "unit": 3
#             },
#             "uplink": {
#               "value": 1,
#               "unit": 3
#             }
#           },
#           "_id": {
#             "$oid": "64da2a78cfb5a5f7deba10ad"
#           },
#           "pcc_rule": []
#         }
#       ],
#       "_id": {
#         "$oid": "64da2a78cfb5a5f7deba10ac"
#       }
#     }
#   ],
#   "access_restriction_data": 32,
#   "subscriber_status": 0,
#   "network_access_mode": 0,
#   "subscribed_rau_tau_timer": 12,
#   "__v": 0
# }
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


class UserInDB(User):
    hashed_password: str

# {'_id': ObjectId('64da2a78cfb5a5f7deba10ab'), 'schema_version': 1, 'imsi': '123456789',
#  'msisdn': ['54654324', '4485499494'], 'imeisv': [], 'mme_host': [], 'mme_realm': [],
#  'purge_flag': [], 'security': {'k': '465B5CE8 B199B49F AA5F0A2E E238A6BC',
#  'op': None, 'opc': 'E8ED289D EBA952E4 283B54E8 8E6183CA', 'amf': '8000'},
#  'ambr': {'downlink': {'value': 1, 'unit': 3}, 'uplink': {'value': 1, 'unit': 3}},
#  'slice': [{'sst': 1, 'default_indicator': True,
# 'session': [{'name': 'internet', 'type': 3,
# 'qos': {'index': 9, 'arp': {'priority_level': 8, 'pre_emption_capability': 1,
# 'pre_emption_vulnerability': 1}}, 'ambr': {'downlink': {'value': 1, 'unit': 3},
# 'uplink': {'value': 1, 'unit': 3}}, '_id': ObjectId('64da2a78cfb5a5f7deba10ad'),
# 'pcc_rule': []}], '_id': ObjectId('64da2a78cfb5a5f7deba10ac')}],
# 'access_restriction_data': 32, 'subscriber_status': 0, 'network_access_mode': 0,
#  'subscribed_rau_tau_timer': 12, '__v': 0}
