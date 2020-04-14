"""
收集用户输入 input
"""

name = input('请问你的姓名：')
age = int(input('请问你的年龄'))
'''
▲输入的数量不是整型，报错！（输入浮点型也报错
但用float() 可以转化整型的值
'''

print(f'Hi {name}, you are {age} now')
