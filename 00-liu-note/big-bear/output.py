print("hello world")

# 输出变量
price = 10
number = 5
print(price, number)
print("总共花费", price*number)

# sep分隔符
print("hello", "world")
print("hello", "world", "hello", "python", sep=",,,")
print("2019", "12", "12", sep="---")
print('124943098', 'qq.com', sep='@')

# end结束符
print('hello')
print('world')
print('hello', end=', ')
print('world')

# file
file_source = open('00-liu-note/big-bear/zen.txt', 'w')
print(
    'Life is short, you need Python',
    file=file_source
)
file_source.close()


# price = int(input('请输入单价:'))
# number = int(input('请输入数量:'))
# print('商品总价是：', price*number)
