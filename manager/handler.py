from dotenv import dotenv_values
import logging
from dao.mongodao import Open5GSdao
from constants.error_message import ErrorMessage
from constants.info_message import InfoMessage
from http_handler.response_handler import ResponseHandler
from fastapi import status


class Reqmanager:
    def __init__(self):
        self.config = dotenv_values(".env")
        self.logger = logging.getLogger(__name__)
        self.dao = Open5GSdao(self.config['DB_COLLECTION_NAME'])

    def find(self, condition: dict):
        res = ResponseHandler()
        try:
            result = self.dao.find(condition)
            self.logger.info(InfoMessage.DB_FIND)
        except Exception as error:
            self.logger.error(ErrorMessage.DB_SELECT)
            self.logger.error(error)
            raise Exception
        if result:
            res.set_response(result)
            res.status_code(status.HTTP_200_OK)
            return res

        res.set_response({"message": InfoMessage.NOT_FOUND})
        res.status_code(status.HTTP_404_NOT_FOUND)

        return res
