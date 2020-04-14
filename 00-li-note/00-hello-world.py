"""
● 注释方法
● 打印方法
"""

# 单行注释 （ Ctrl+/
print('Hello World')  # 单行注释（在尾部）

'''
● 用三个“单引号”进行多行注释
● 三个“双引号”也可以
'''

print('I', 'love', 'you', sep='___')  # sep=''用于指定打印的多个元素用什么来分隔
print('Hello', end=', ')  # end='' 用于指定打印后跟随的字符（默认\n即换行
print('my friend')

theFile = open('00-li-note/others/txt01.txt', 'w', encoding="utf-8")
print('人生苦短，我用 python\nLife is short, you need Python', file=theFile)  # file= 用于指定将内容打印到哪个文件
theFile.close()

#字符串大小写转换
str.title(I LOVE PYTHON)
str. capitalize(I LOVE PYTHON)
str. swapcase(I LOVE PYTHON)

str = "love python"
str.count('o')

str= 'love python'
str.starstswith('o')
str = 'love python'
str.endswith('n')