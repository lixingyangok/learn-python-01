# 已经转移 2022.03.05 20:51:12 星期六

string01 = '零一二三四五六七八九'
string02 = string01[:]
string03 = 'Hello world'

print('[1]: ', string01[1])
print('[-1]', string01[-1])
print('[:3]', string01[:3])
print('[1:3]', string01[1:3])
print('[1:]', string01[1:])
print(f'Str: {string03}, and len() = {len(string01)}')
print(f'Str.upper(): {string03.upper()}')  # 大小写转换不会改变原有值
print(f'Str.lower(): {string03.lower()}')
print(f'Str.title(): {string03.title()}')
print(f'Str.find(): {string03.find("Hello")}')
print(f'Str.replace(): {string03.replace("Hello", "Hi")}')  # 字符替换不能转变原有值
print(f'someStr in Str: {"Hello" in string03}')
