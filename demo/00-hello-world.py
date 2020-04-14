string01 = 'hello world, I\'m Li.\n'
string02 = '''
hello world, I'm Li.
hello world, I'm Li.
'''
print(string01 * 2)
print(string02)

birth_year = input('What year were you born in?')
age = 2020 - int(birth_year)  # 转换字符为数字
print('You are now: ' + str(age))  # 转换数字为字符
