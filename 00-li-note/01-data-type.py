"""
数据类型检测方法
● type(18)  # <class 'int'>
● isinstance(18, int)  # True
"""

name = 'Tom'
number = 18

print('name的数据类型：', type(name))
print('number的数据类型：', type(number))

typeStr = type(1)
print('type()返回的值，类型是：', type(typeStr))

print('■'*20)

print('查看18是不是整型：', isinstance(18, int))
print('查看18是不是浮点型：', isinstance(18, float))


