# import logging
# import os
# import colorlog
# from logging.handlers import RotatingFileHandler
# from datetime import datetime
#
# cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前项目路径
# log_path = os.path.join(os.path.dirname(cur_path), 'logs')  # log_path为存放日志的路径
# if not os.path.exists(log_path): os.mkdir(log_path)  # 若不存在logs文件夹，则自动创建
#
# log_colors_config = {
#     # 终端输出日志颜色配置
#     'DEBUG': 'white',
#     'INFO': 'cyan',
#     'WARNING': 'yellow',
#     'ERROR': 'red',
#     'CRITICAL': 'bold_red',
# }
#
# default_formats = {
#     # 终端输出格式
#     'color_format': '%(log_color)s%(name)s当前时间:%(asctime)s-当前文件:%(filename)s-第%(lineno)d行-日志级别:%(levelname)s-日志信息:%(message)s',
#     # 日志输出格式
#     'log_format': "%(name)s当前时间:%(asctime)s-当前文件:%(filename)s-第%(lineno)d行-日志级别:%(levelname)s-日志信息:%(message)s"
# }
#
#
# class HandleLog:
#     """
#     先创建日志记录器（logging.getLogger），然后再设置日志级别（logger.setLevel），
#     接着再创建日志文件，也就是日志保存的地方（logging.FileHandler），然后再设置日志格式（logging.Formatter），
#     最后再将日志处理程序记录到记录器（addHandler）
#     """
#
#     obj = None
#
#     def __init__(self,name):
#         self.__now_time = datetime.now().strftime('%Y-%m-%d')  # 当前日期格式化
#         self.__all_log_path = os.path.join(log_path, self.__now_time + "-all" + ".log")  # 收集所有日志信息文件
#         self.__error_log_path = os.path.join(log_path, self.__now_time + "-error" + ".log")  # 收集错误日志信息文件
#         self.__logger = logging.getLogger(name=name)  # 创建日志记录器
#         self.__logger.setLevel(logging.DEBUG)  # 设置默认日志记录器记录级别
#         self.__logger.propagate =False
#
#
#     @staticmethod
#     def __init_logger_handler(log_path):
#         """
#         创建日志记录器handler，用于收集日志
#         :param log_path: 日志文件路径
#         :return: 日志记录器
#         """
#         # 写入文件，如果文件超过1M大小时，切割日志文件，仅保留3个文件
#         logger_handler = RotatingFileHandler(filename=log_path, maxBytes=1 * 1024 * 1024, backupCount=3, encoding='utf-8')
#         return logger_handler
#
#     @staticmethod
#     def __init_console_handle():
#         """创建终端日志记录器handler，用于输出到控制台"""
#         console_handle = colorlog.StreamHandler()
#         return console_handle
#
#     def __set_log_handler(self, logger_handler, level=logging.DEBUG):
#         """
#         设置handler级别并添加到logger收集器
#         :param logger_handler: 日志记录器
#         :param level: 日志记录器级别
#         """
#
#         logger_handler.setLevel(level=level)
#         self.__logger.addHandler(logger_handler)
#
#     def __set_color_handle(self, console_handle):
#         """
#         设置handler级别并添加到终端logger收集器
#         :param console_handle: 终端日志记录器
#         :param level: 日志记录器级别
#         """
#         console_handle.setLevel(logging.DEBUG)
#         self.__logger.addHandler(console_handle)
#
#
#     @staticmethod
#     def __set_color_formatter(console_handle, color_config):
#         """
#         设置输出格式-控制台
#         :param console_handle: 终端日志记录器
#         :param color_config: 控制台打印颜色配置信息
#         :return:
#         """
#         formatter = colorlog.ColoredFormatter(default_formats["color_format"], log_colors=color_config)
#         console_handle.setFormatter(formatter)
#
#     @staticmethod
#     def __set_log_formatter(file_handler):
#         """
#         设置日志输出格式-日志文件
#         :param file_handler: 日志记录器
#         """
#         formatter = logging.Formatter(default_formats["log_format"], datefmt='%a, %d %b %Y %H:%M:%S')
#         file_handler.setFormatter(formatter)
#
#     @staticmethod
#     def __close_handler(file_handler):
#         """
#         关闭handler
#         :param file_handler: 日志记录器
#         """
#         file_handler.close()
#
#     def __console(self, level, message):
#         """构造日志收集器"""
#         all_logger_handler = self.__init_logger_handler(self.__all_log_path)  # 创建日志文件
#         error_logger_handler = self.__init_logger_handler(self.__error_log_path)
#
#         console_handle = self.__init_console_handle()
#
#         self.__set_log_formatter(all_logger_handler)  # 设置日志格式
#         self.__set_log_formatter(error_logger_handler)
#         self.__set_color_formatter(console_handle, log_colors_config)
#
#         self.__set_log_handler(all_logger_handler)  # 设置handler级别并添加到logger收集器
#         self.__set_log_handler(error_logger_handler, level=logging.ERROR)
#         self.__set_color_handle(console_handle)
#
#         if level == 'info':
#             self.__logger.info(message)
#         elif level == 'debug':
#             self.__logger.debug(message)
#         elif level == 'warning':
#             self.__logger.warning(message)
#         elif level == 'error':
#             self.__logger.error(message)
#         elif level == 'critical':
#             self.__logger.critical(message)
#
#         self.__logger.removeHandler(all_logger_handler)  # 避免日志输出重复问题
#         self.__logger.removeHandler(error_logger_handler)
#         self.__logger.removeHandler(console_handle)
#
#         self.__close_handler(all_logger_handler)  # 关闭handler
#         self.__close_handler(error_logger_handler)
#
#     def debug(self, message):
#         self.__console('debug', message)
#
#     def info(self, message):
#         self.__console('info', message)
#
#     def warning(self, message):
#         self.__console('warning', message)
#
#     def error(self, message):
#         self.__console('error', message)
#
#     def critical(self, message):
#         self.__console('critical', message)
#
#
# log = HandleLog(__name__)
#
# if __name__ == '__main__':
#     for i in range(2):
#         log.info("这是日志信息")
#         log.debug("这是debug信息")
#         log.warning("这是警告信息")
#         log.error("这是错误日志信息")
#         log.critical("这是严重级别信息")


import logging
from threading import Thread
import colorlog
default_formats = {
    # 终端输出格式
    'color_format': '%(log_color)s%(name)s当前时间:%(asctime)s-当前文件:%(filename)s-第%(lineno)d行-日志级别:%(levelname)s-日志信息:%(message)s',
    # 日志输出格式
    'log_format': "%(name)s当前时间:%(asctime)s-当前文件:%(filename)s-第%(lineno)d行-日志级别:%(levelname)s-日志信息:%(message)s"
}
log_colors_config = {
    # 终端输出日志颜色配置
    'DEBUG': 'white',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}
class SQLEngine(object):

    def __init__(self,name=__name__):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # formatter = logging.Formatter('%(asctime)s:%(thread)d - %(name)s - %(levelname)s - %(message)s')
        formatter = colorlog.ColoredFormatter(default_formats["color_format"], log_colors=log_colors_config)
        ch.setFormatter(formatter)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(ch)

    def debug(self,SQL,):
        self.logger.debug(SQL)
        # print (SQL)
    def info(self,SQL,):
        self.logger.info(SQL)
    def error(self,SQL,):
        self.logger.error(SQL)

class HandleLog(Thread):
    def __init__(self, name, logengine):
        Thread.__init__(self)
        self.name = name
        self.logger = logengine

    def run(self):
        #db = SQLEngine('')
        self.logger.execute('select 1,2')

if __name__ == '__main__':
    logger = SQLEngine('')
    HandleLog('thread 1', logger).start()
    HandleLog('thread 2', logger).start()
