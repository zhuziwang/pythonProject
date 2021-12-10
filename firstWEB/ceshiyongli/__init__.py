class Animal:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

    def __str__(self):
        return '我的名字是%s,我的颜色为%s'%(self.name,self.colour)
    def ceshi(self,foot):
        return '出现名字应该是zhangsan,实际是%s,实际颜色是%s,吃%s'%(self.name,self.colour,foot)
dog = Animal('旺财','white')
print(dog)
# dog2=Animal.ceshi('2','3')
# print(dog2)
#dog.ceshi('肉')
print(dog.ceshi('肉'))

dog2 = Animal('旺财2','white2')
print(dog2)
print(dog2.ceshi('肉2'))

print(dog)
