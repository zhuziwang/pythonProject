from selenium import webdriver

class WebKey:

    def __init__(self):
        self.driver = None

    def openbrwser(self,br='gc'):
        '''
        打开浏览器
        :param br: gc=谷歌浏览器；ff=Firefox浏览器；ie=IE浏览器
        :return:
        '''
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver == webdriver.Firefox()
        elif br == 'ie':
            self.driver == webdriver.Ie()
        else:
            print('浏览器暂不支持！请在此添加实现代码')

        #默认隐式等待20s
        self.driver.implicitly_wait(20)

    def geturl(self,url=None):
        '''
        打开网站
        :param url: 网站地址
        :return:
        '''
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh = webdriver.Chrome().refresh()

    def xpath(self,locator=''):
        '''
        找到xpath
        :param locator: 定位器
        :return:
        '''
        ele = None
        self.ele = None
        ele = self.driver.find_element_by_xpath(locator)
        self.ele = ele
        return ele

    def click(self,locator=None):
        '''
        找到，并点击元素
        :param locator: 定位器，默认xpath
        :return:
        '''
        ele = self.xpath(locator)
        ele.click()

    def input(self,locator=None,value=None):
        '''
        找到元素，并完成输入
        :param locator: 定位器，默认xpath
        :param value: 需要输入字符串
        :return:
        '''
        ele = self.xpath(locator)
        ele.send_keys(str(value))

    def intoiframe(self,locator=None):
        '''
        进入iframe
        :param locator: 定位器，默认xpath
        :return:
        '''
        ele = self.xpath(locator)
        self.driver.switch_to.frame(ele)

