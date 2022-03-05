# 已经转移 2022.03.05 20:51:12 星期六
from datetime import datetime 

string01 = 'hello world, I\'m Li.\n' * 2 # 可以用乘法
string02 = '''
hello world, I'm Li.
hello world, I'm Li.
'''
print(string01)
print(string02)


birth_year = input('What year were you born in?')
age = datetime.now().year - int(birth_year)  # 字符串 -> 数字
sAgeVal = str(age) # 数字 -> 字符串
print(f'\nGreat! \nYou are: {age} years old now')  # 转换数字为字符


