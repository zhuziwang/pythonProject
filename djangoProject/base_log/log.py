# -*- coding:utf-8 -*-

import logging
import time
from ..settings import BASE_DIR
from logging import handlers

class Log():

    def __init__(self, level="DEBUG"):
        '''
        日志器对象
        :param level: 级别
        name 默认为空：root
        '''

        self.log = logging.getLogger()
        self.log.setLevel(level)

    def   console_handle(self,level="DEBUG"):
        '''
        控制台处理器
        :param level:
        :return:
        '''

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        # 处理器格式
        console_handler.setFormatter(self.get_formatter()[0])
        return console_handler

    def file_handle(self,level="DEBUG"):
        '''文件处理器'''

        str_time = self.get_str_time()
        BASE_DIR_PATH = str(BASE_DIR)
        file_handler = logging.FileHandler(BASE_DIR_PATH+'\\djangoProject\\base_log\\' +str_time + '-log.txt', mode='a',encoding="utf-8")
        file_handler.setLevel(level)
        # 处理器格式
        file_handler.setFormatter(self.get_formatter()[1])
        return file_handler

    def get_formatter(self):
        '''格式器'''

        # 定义输出格式
        fmt1 = "%(asctime)s--->%(name)s--->%(levelname)s--->%(message)s--->%(filename)s：%(lineno)d"
        fmt2 = "%(asctime)s--->%(name)s--->%(levelname)s--->%(message)s--->%(filename)s：%(lineno)d"
        console_fmt = logging.Formatter(fmt1)
        file_fmt = logging.Formatter(fmt2)
        return console_fmt,file_fmt

    def get_log(self):
        # 日志器添加控制台处理器
        self.log.addHandler(self.console_handle())
        # 日志器添加文件处理器
        self.log.addHandler(self.file_handle())
        return self.log

    def get_str_time(self):
        str_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        str_time = str(str_time)
        return str_time



