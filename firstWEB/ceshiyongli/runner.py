
import os
import pytest
from firstWEB.ceshiyongli.params import datas
print(datas)

pytest.main(['-s','firstWEB/ceshiyongli/login/login.py','--alluredir','./temp','-s'])
os.system('allure generate ./temp -o ./ report --clear')