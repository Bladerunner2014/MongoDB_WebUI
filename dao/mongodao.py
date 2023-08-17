import pymongo
import logging
import pymongo.errors
from db.db_connection import DBconnect
from constants.error_message import ErrorMessage
import json
from bson import json_util


logger = logging.getLogger(__name__)


class Open5GSdao:

    def __init__(self, collection_name):
        self.db = DBconnect(collection_name).connect()

    def insert_one(self, query: dict):
        try:
            return json.dumps(self.db.insert_one(query))
        except pymongo.errors as error:
            logger.error(ErrorMessage.DB_INSERT)
            logger.error(error)
            raise error

    def find(self, condition: dict):
        try:
            dt = self.parse_json(self.db.find_one(condition))
            return dt
            # return self.db.find_one(condition)
        except pymongo.errors as error:
            logger.error(ErrorMessage.DB_SELECT)
            logger.error(error)
            raise error

    def update(self, fltr: dict, new_values: dict):
        try:
            self.db.update_one(fltr, new_values)
        except pymongo.errors as error:
            logger.error(ErrorMessage.DB_UPDATE)
            logger.error(error)
            raise error

    def delete(self, imsi: dict):
        try:
            self.db.delete_one(imsi)
        except pymongo.errors as error:
            logger.error(ErrorMessage.DB_DELETE)
            logger.error(error)
            raise error

    @staticmethod
    def parse_json(data):
        return json.loads(json_util.dumps(data))
