
# # 加法运算符
# number1 = int (input('请输入第一个数'))
# number2 = int (input('请输入第二个数'))
# print(number1+number2)
# print (type(number1))
#
# s1 = 'hello'
# s2 = 'world'
# print(s1+s2)

# 乘法运算符 *
print('='*10)
print(''*2+'△'+''*2)
print(''+'△'*3+'')
print('△'*5)

# # 除法运算符 /
# a = 10
# b = 0
# print(a/b)

# # 向下取整运算符 //
# # a = 10
# # b = 3
# # print(a/b)
# # print(a//b)
# #
# # # 余数运算符 %  a % b → r = a - b*(a//b)
# # print(10/3)
# # print(10%3)
# # print(3/10)
# # print(3%10)
# # print(-10%3)
# # print(10%-3)

# 赋值运算符 =
a = b= 5
print(a,b)
a,b=5,10
print(a,b)
a = 5
b = 10
a,b = b,a    #快速交换
print(a,b)

# 复合赋值运算符
a = 5
a += 2 # a = a+2
print(a)
b = 10
b *= 5 # b = b*5
print(b)