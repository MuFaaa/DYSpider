import redis

from general_purpose.setting import *


class RedisClient(object):
    def __init__(self, key, redis_host=REDIS_HOST, redis_port=REDIS_PORT,redis_password=None):
        """
        初始化Redis链接
        :param 数据库的键值:
        :param value:
        """
        self.db = redis.StrictRedis(host=redis_host, port=redis_port,password=redis_password)
        self.key = key

    def name(self):
        return "{}".format(self.key)

    def set(self, value=None):
        """
        存储数据为hash类型
        :param username:
        :param value:
        :return:
        """
        return self.db.sadd(self.name(), value)

    def delete(self, value=None):
        """
        根据简明删除键值对
        :param value:
        :param username:
        :return:
        """
        return self.db.srem(self.name(), value)

    def getall(self):
        """
        获取键名里所有成员
        :param username:
        :return:
        """
        return self.db.smembers(self.name())

    def getone(self):
        """
        移除一个元素并返回这个元素
        :param username:
        :return:
        """
        return self.db.spop(self.name())

    def judge(self, username=None, value=None):
        """
        判断某元素是否在某个集合中
        :param username:
        :param value:
        :return:
        """
        return self.db.sismember(name=username, value=value)

    def timeout(self, value=None):
        """
        设置超时时间
        :param value:
        :return:
        """
        return self.db.expire(self.name(), value)

    def save_key(self, value=None, time=None):
        """
        保存zst类型的key
        :param value:
        :param time:
        :return:
        """
        return self.db.zadd(self.name(), {value: time})

    def del_key(self, data_min=None, data_max=None):
        """
        删除指定范围zset类型的key
        :param data_min:
        :param data_max:
        :return:
        """
        return self.db.zremrangebyscore(self.name(), data_min, data_max)

    def get_key(self, data_min=None, data_max=None):
        """
        返回指定范围所有的zset类型的key
        :param data_min:
        :param data_max:
        :return:
        """
        return self.db.zrangebyscore(self.name(), data_min, data_max)

    def del_assign_key(self, value=None):
        """
        删除zset指定值
        :param value:
        :return:
        """
        return self.db.zrem(self.name(), value)


