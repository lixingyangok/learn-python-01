'''
Author: 李星阳
Date: 2022-02-20 19:42:44
LastEditors: 李星阳
LastEditTime: 2022-02-26 16:10:59
Description: 
'''

str01 = 'let\'s go' # 用 \ 转义

print('str01：', str01)

print('type：', isinstance(str01, str)) # True
print('type：', type(str01)) # <class 'str'>
print('type：', type(type(str01))) # <class 'type'>

print(
    '\n大小写转换：',
    str.swapcase('I love PYTHON'), # 逐字母大小逆转
    str.title('I love the PYTHON'), # 逐个个单词首大写
    str.capitalize('I love PYTHON'), # 逐句首字母大写
    sep='\n'
)

print(
    '\n字符包含性研究：',
    'hello'.count('l'), # 包含 2 个 l
    'hello'.startswith('he'), # True
    'hello'.endswith('o'), # True
    sep='\n',
)

