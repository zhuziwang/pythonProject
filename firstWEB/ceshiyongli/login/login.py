import pytest
from firstWEB.ceshiyongli.webkeys import WebKey


class Test_Commerce:

    def setup_class(self):
        self.web = WebKey()
        self.web.openbrwser()
    @pytest.mark.parametrize('listcases')
    def test_login(self,listcases):
        # self.web.geturl('http://my.kouyu100.com/demo0')
        # self.web.openbrwser().refresh()
        testcase = listcases['cases']
        for cases in testcase:
            listcase = list(cases.values())   #把字典转成列表值
            func = getattr(self.web,listcase[1])
            values= cases[2:]
            func(*values)