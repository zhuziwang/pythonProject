from selenium import webdriver
import xlrd
# 导入excel表
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class B:
    '''
     username:用户名
     password:密码
     return
    '''
    def loginner(self):
     self.driver = webdriver.Chrome()
     self.driver.get("http://my.kouyu100.com/demo0")
     sleep(5)
     self.driver.find_element_by_xpath('//*[@id="mainLoginForm"]/div[1]/div[1]/input').send_keys(123)
     self.driver.find_element_by_xpath('//*[@id="mainLoginForm"]/div[1]/div[2]/input').send_keys(password)

if __name__ == '__main__':
    B=B()
    B.loginner()