#第二部分-列表和元祖
#列表类似于集合的概念，列表长度
bicycles = ['treck', 'cannondale', 'redline', 'specicalized']
print(bicycles)
print(len(bicycles))
#索引从0开始而不是从1开始，最后一个元素是-1
a = [1,72,-36,999,1025,-100]
print(a[2])
print(a[0])
print(a[-1])
#修改列表里的元素
a[2] = 100
print(a)
#使用列表里的值
message = f'my first bike was a {bicycles[0].title()}.'
print(message)
#添加和删除
a.append(120)
a.extend(bicycles)
a.insert(0,-20)

del a[0]
print(a)

popped_a = a.pop()
print(a)
print(popped_a)

first_owner = a.pop(0)
print(f'the number is {first_owner}.')

b = 'redline'
a.remove(b)
print(a)
print(f'\nA {b.title()} is too expensive.')
#列表的排序：永久和临时
car = ['bmw', 'byd', 'audi', 'mini', 'subaru', 'toyota']
car.sort()
print(car)
car.sort(reverse=True)
print(car)

print("Here is the original list.")
print(car)
print('\nHere is the sorted list:')
print(sorted(car))
print('\nHere is the original list again:')
print(car)

car.reverse()
print(car)
#操作列表
#for 循环
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()},that was a great trick.')
    print(f"I can't wait to see you next time,{magician.title()}.\n")
print('thank your performance.')
#数值列表（左闭右开）
for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)
noy = list(range(2,11,2))
print(noy)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)
#列表中的统计计算和推导式
digs = [1,2,3,4,5,6,7,8,9,10]
print(min(digs))
print(max(digs))
print(sum(digs))

squares = [value**2 for value in range(1,11)]
print(squares)  
#使用列表的一部分
#切片以及遍历切片
players = ['charles','meta','michal','eli','florence']
print(players[0:3])
print(players[:4])
print(players[-3::1])

print('Here are the three players of the team:')
for player in players[:3]:
    print(players.title())
print(list[::-1])
#复制列表
MyFoods = ['pizza','falafel','carrot']
friendsFoods = MyFoods[:]

MyFoods.append('cannoli')
friendsFoods.append('ice cream')

print('My favourite foods are:')
print(str(MyFoods))
print('\nMy friends favourite foods are:')
print(str(friendsFoods))
#元组 不能修改 由逗号标识，只是圆括号简洁
#定义和修改元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print('original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensiond = (400,100)
print('\nModified dimensions:')
for dimension in dimensiond:
    print(dimension)

myT = (3,)
print(myT)