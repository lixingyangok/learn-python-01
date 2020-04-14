"""
字符串相关
"""

str01 = '〇一二三四五六七八九'
print(str01[1:-1])  # 砍头去尾得到：一二三四五六七八

str02 = ' ■ '.join(['baidu', 'com'])  # 连接数组
str03 = ' ● '.join(('Tom', 'Jack'))  # 连接元组
print(str02, '    ', str03)

str04 = 'i love PYTHON. how about YOU?'
print(
    f'■■大小写转换{"■"*30}',
    str04.upper(),  # 全大写
    str04.lower(),  # 全小写
    str04.title(),  # 各单词首字母大写
    str04.capitalize(),  # 字符串首字母大写
    str04.swapcase(),  # 大小写反转
    sep='\n',
)

print(
    f'■■字符查找{"■"*30}',
    f'找到o有：{str04.count("o")}个',  # 查询字符出现的次数（大小写敏感，所以得到结果：3
    f"找到l在：第{str04.find('l')}位",  # 查询字符的索引位置（找不到返回-1
    f"找到l在：第{str04.index('l')}位",  # 查询字符的索引位置（找不到会抛出异常!!!
    str04.startswith('i'),  # 查询是否以某字符开头
    str04.endswith('?'),  # 查询是否以某字符结尾
    sep='\n',
)

str05 = '''
人生 苦短
我用 Python 
你喜欢 Python 吗
'''.strip()

print(
    f'■■字符分割{"■"*30}',
    str05.split(),  # 默认用空白字符分割（如空格，换行等，分割符号消失
    str05.split('Python', 1),  # 2参为分割次数（分割符号消失
    str05.partition('Python'),  # 切成【元组】（分割符号保留
    sep='\n',
)

str06 = ' 你好-世界 '
print(
    f'■■字符修剪{"■"*30}',
    f'■{str06.strip()}■',
    f'■{str06.lstrip()}■',
    f'■{str06.rstrip()}■',
    sep='\n',
)