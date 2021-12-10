from __future__ import  unicode_literals

import dic as dic
from django.shortcuts import render
from .models import cal,MYSQL
from django.http import HttpResponse
from .ceshiyongli import fun
from selenium import webdriver






def index(request):
    return render(request, '../templates/index.html')     #render:渲染网页

def CalPage(request):
    return render(request, '../templates/cal.html')

def Cal(request):
    if request.method == 'POST':
        value_a = request.POST['valueA']
        value_b = request.POST['valueB']
        result=int(value_a) + int(value_b)
        # cal.objects.create(value_a=value_a,value_b=value_b,result=result)
        return render(request, '../templates/result.html', context={'data':result})
    else:
        return HttpResponse('please visit us with POST')

def CalList(request):
    data = cal.objects.all()        #取全部数据
    # for i in data:
    #     print(data.value_a,data.value_b,data.result)
    return render(request, '../templates/list.html', context={'data': data})

def DelData(request):
    cal.objects.all().delete()
    return HttpResponse('data Delted')  #服务器给前端返回值HttpResponse

# global url
# global name
# global password
# global browser

def login_selenium(request):
    return render(request, '../templates/login_selenium.html')
def login_selenium_run(request):
    if request.method == 'get':
        return render(request, '../templates/login_selenium.html')
    if request.method == 'POST':

        # DATABASE = request.POST['DATABASE']
        table=request.POST['table']
        title=request.POST['url']
        uname=request.POST['name']
        ukey=request.POST['password']
        value1=request.POST['value1']
        value2=request.POST['value2']
        value3=request.POST['value3']
        value4=request.POST['value4']
        value5=request.POST['value5']
        value6=request.POST['value6']
        value7=request.POST['value7']
        value8=request.POST['value8']
        value9=request.POST['value9']
        value10=request.POST['value10']

        mysql=MYSQL()
        # add_sql=mysql.create_sql(DATABASE)
        # mysql.sql(add_sql)

        add_sql = mysql.insert_into(table,title,uname,ukey,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10)
        mysql.sql(add_sql)
        print(url,name,password,browser)
        dic={'url':url,'name':name,'password':password,'browser':browser}



        return render(request,'login_selenium_run.html',dic)
    #
    # else:
    #     return HttpResponse('please visit us with POST')
#
#调用浏览器
#


# def login_sql(request):
#  #execute()  执行原生sql
#     SQL.cursor.execute("select name from login_selenium where type = '1'")
#     row = SQL.cursor.fetchall()
    # for rows in row:
    #     print (rows)
    # print (row)
    # return render(request,'login_selenium.html',context={'row': row})
    #
    # SQL.cursor.execute("select type from login_selenium group by type")
    # type[i] = SQL.cursor.fetchall()
    # print(type[i])
    # if 0==type[i]:
    #     type='教师'
    # elif 1==type[i]:
    #     type='学生'
    # else:
    #     type='其他'
    # return render(request,'login_selenium.html',context={'type': type})

#自动处理全局错误，遇到错误打印，继续执行
try:
    #可能出现错误的代码块
    print('aa')
    pass
except Exception as msg:
    #出现错误执行的代码块
    print(msg)
    def error_html(request):
        return render(request, '../templates/Erro_html.html')
    error_html=error_html()
    pass
else:
    print('没有错误的代码快')
finally:
    print('不管有没有出错都执行的代码块')
