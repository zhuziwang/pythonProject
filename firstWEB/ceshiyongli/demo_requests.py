import requests

Session=requests.session()
Session.Windows_Edge_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55',
         'Accept-Encoding': 'gzip, deflate, br',
         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
         'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"'
         }
Session.payloald={'domain': 'demo0',
          'userName': 'a30',
          'userPwd': 'bc4e3640e5e1014755617651d6ac368d'
          }
req=Session.post('https://my.kouyu100.com/demo0/getTokenFromServer.action',
                 data=Session.payloald,
                 headers=Session.Windows_Edge_headers
                 )
print(req.text)
print(req.url)
print(req.headers)
#req.request.headers：返回requests发送的内容
print(req.request.headers)
print(req.status_code)
print(req.cookies)
print(req.cookies['authToken'])
Cookies_dict=dict(authToken=req.cookies['authToken'])
print('cookies_dict的值是：%s'%Cookies_dict)

req2=Session.post('http://my.kouyu100.com/demo0/findDictWordsByLetter.action')
print(req2.text)
print(req2.status_code)
print(req2.headers)
print(req2.url)
print(req2.cookies)
print(type(req2.text))
string='299788,299809,299800,299804,299797'
if string in req2.text:
    print('接口正确')
else:
    print('接口错误')