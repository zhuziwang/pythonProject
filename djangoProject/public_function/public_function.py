# -*- coding:utf-8 -*-

import pickle,base64
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import os
import time

from djangoProject.base_log.log import Log

class PublicFunction():
    '''项目的公用方法'''

    def __init__(self):
        log = Log()
        self.logger = log.get_log()

    def get_str_time(self):
        str_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        str_time = str(str_time)
        return str_time

    def windows_screenshot(self,url):
        '''
        谷歌浏览器打开一个网页并截图保存
        :param url:
        :return: 图片
        '''

        driver= webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.get(url)
        driver.maximize_window()
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        try:
            driver.get_screenshot_as_file('public_function\\windows_screenshot_image\\'+picture_time+'.png')
            self.logger.info('截图成功')
        except BaseException as msg:
            self.logger.debug(msg)
        return picture_time+'.png'


class CookiesSecret(object):
    @staticmethod
    def dumps(data):
        data_bytes = pickle.dumps(data)
        base64_bytes = base64.b64encode(data_bytes)     # pickle编码，返回字节类型
        return base64_bytes.decode()        # b64编码

    @staticmethod
    def loads(data):
        base64_bytes = base64.b64decode(data)       # b64解码
        obj = pickle.loads(base64_bytes)        # pickle解码，返回字符串
        return obj
