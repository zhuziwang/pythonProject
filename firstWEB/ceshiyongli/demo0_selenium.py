from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from .webkeys import WebKey

#driver=webdriver.Chrome()
#driver.implicitly_wait(20)



class Test_Comm:

    def setup_class(self):
        self.web = WebKey()
        self.web.openbrwser()

    def browser(self):
        self.web.geturl('http://my.kouyu100.com/demo0')
        self.web.refresh()
        driver.set_window_size(1280,720)
    def login():
        user_name=driver.find_element_by_xpath('//*[@id="mainLoginForm"]/div[1]/div[1]/input')
        user_name.clear()
        user_name.send_keys('a30')
        passworld=driver.find_element_by_xpath('//*[@id="mainLoginForm"]/div[1]/div[2]/input')
        passworld.clear()
        passworld.send_keys('ky100yanshi')
        driver.find_element_by_id('id="btnAutoLogin').clear()
    def print_asserted_information():
        title=driver.title
        print(title)
        now_url=driver.current_url
        print(now_url)
        user_name=driver.find_element_by_id('username').text()
        print(user_name)
        school_class=driver.find_element_by_id('id="classname"')
        cookies=driver.get_cookies()
        print(cookies)
    def practice():
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div/span[2]').click()
        Parent_communication=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/ul/li[2]/a/img')
        print('返回元素的尺寸(图片)：%s',Parent_communication.size)
        print('获取元素的文本(图片)：%s',Parent_communication.text)
    #获取悬浮显示文字
        task=driver.find_element_by_xpath('//*[@id="slides"]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/a')
        AC_move_to_element=ActionChains(driver).move_to_element(task).perform()
        print('悬停显示内容：%s',AC_move_to_element)
    #悬浮显示结束
        driver.find_element_by_link_text('课表').click()
        driver.back()

        Personal_space=driver.find_element_by_xpath('//*[@id="nav"]/li[6]/a')
        ActionChains(driver).move_to_element(Personal_space).perform()
        driver.find_element_by_xpath('//*[@id="nav"]/li[6]/ul/li[4]/a').click()
        Search_name=driver.find_element_by_id('perkey')
        Search_name.send_keys('测试删除')
        Search_name.send_keys(Search_name.BACK_SPACE)
        sleep(2)
        Search_name.send_keys('测试空格键')
        Search_name.send_keys(Search_name.SPACE)
        sleep(2)
        Search_name.send_keys(Search_name.TAB)
        sleep(2)
        Search_name.send_keys(Search_name.ESCAPE)
        sleep(2)
        try:
            Search_name.clear()
            Search_name.click()
            Search_name.send_keys(Search_name.ENTER)
            pass
        except Exception as msg:
            driver.get_screenshot_as_file('E:\pycharm\Error_img')
            print(msg)
            pass
        finally:
            driver.refresh()
            driver.back()

        customer_service=driver.find_element_by_xpath('//*[@id="onlineService"]/div[1]/ul/li/a/img')
        sreach_windows=driver.current_window_handle
        customer_service.click()
        all_handles=driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                driver.switch_to.window(handle)
                sleep(2)
                pass
            pass
        now_sreach_windows=driver.current_window_handle
        if sreach_windows==now_sreach_windows:
            print('窗口跳转到了之前的个人中心也没')
        else:
            print('窗口跳转到了客服页面')




    driver.quit()

if __name__ == 'main':
    browser()
    login()
    print_asserted_information()
    practice()