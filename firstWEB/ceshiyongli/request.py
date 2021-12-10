import requests
from bs4 import BeautifulSoup
class Douban:
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.starnum =[]
        #从start_num到range,从0到251,步长25
        for start_num in range(0,251,25):
            self.starnum.append(start_num)
        self.head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'}

    def get_top250(self):
        for start in self.starnum:
            #int格式转换为str
            start = str(start)
            #params:url后跟的地址    heads:请求头（模拟浏览器）
            html = requests.get(self.url, params={'start':start},heads=self.head)
            #用BeautifulSoup把网页转换为文本，解析方式为html.parser
            soup = BeautifulSoup(html.text,"html.parser")
            #用的select方法
            name = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            for name in name:
                #只打印文本格式内容，把其他网站前端格式屏蔽
                print(name.get_text())

if __name__== "main":
    cls = Douban()
    cls.get_top250()