def login_sel():
    from selenium import webdriver
    import time
    from .models import SQL
    a=SQL.cursor.execute("select name from login_selenium where id=1")  #取到了查询结果的游标
    xpath1 = SQL.cursor.fetchone()
    print('我是{}'.format(xpath1))
    #xpath1 = SQL.cursor.fetchone()   #把取到的结果给了xpath
    #print(xpath1)
    (xpath1,)=xpath1

    b = SQL.cursor.execute("select name from login_selenium where id=2")
    send = SQL.cursor.fetchone()
    (send,)=send

    c = SQL.cursor.execute("select name from login_selenium where id=3")
    xpath2 = SQL.cursor.fetchone()
    (xpath2,) = xpath2

    # 数据库查询，cursor用来接收返回值的方法fetchall()与fetchone()，fetchmany() 的区别
    # fetchall(self): 接收全部的返回结果行.
    # fetchone(self): 返回一条结果行.
    #单条数据情况中fetchall,fetchone，（self,）下数据一致
    # fetchmany(self, size=None): 接收size条返回结果行.如果size的值大于返回的结果行的数量, 则会返回cursor.arraysize条数据.

    print(xpath1,send,xpath2)
    # send='123'
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    time.sleep(2)
    driver.find_element_by_xpath(xpath1).send_keys(send)
    driver.find_element_by_xpath(xpath2).click()
    print(xpath1, send, xpath2)
    time.sleep(2)
