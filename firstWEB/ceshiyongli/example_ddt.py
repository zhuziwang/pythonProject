class A():
    def a(self,p1):
        print('完成功能a' + str(p1))
        return 'PASS','相关信息'

    def b(self,p1,p2):
        print('完成功能b' + str(p1))
        print(p2)
        return 'PASS', '相关信息'
    def c(self,p1,p2,p3):
        print('完成功能b' + str(p1))
        print(p2)
        print(p3)
        return 'PASS', '相关信息'

params=[
    ['a','aaa'],
    ['b','bbb''bbb'],
    ['c','cccc''cccc','cccc']
]


obj = A()               #把类A给obj
for p in params:            #循环params给p
    #从对象obj获取到一个叫obj的属性或者方法
    func = getattr(obj,p[0])    #自定义变量func，把params中的第一个数据给obj类，作为obj类的方法名，给了func
    func(*p[1:])        #把params中的数据从第二到最后一个给了func方法，当作方法的传参