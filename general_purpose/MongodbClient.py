import pymongo

from general_purpose.setting import *


class MongoDBClient(object):
    def __init__(self, database, dataset):
        """
        初始化Redis链接
        :param 数据库的键值:
        :param value:
        """
        self.client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        self.db = eval('self.client.{}'.format(database))
        self.dataset = eval('self.db.{}'.format(dataset))

    def sert(self, value=None):
        return self.dataset.insert_one(value)
