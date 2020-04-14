# print("hello world 123456")
# message= ("hello")
# print(message)

# ''''''
# username=input('请输入用户名')
# password=input('请输入密码')
# print('您输入的用户名是:',username)
# print('您输入的密码是:',password)
# ''''''

# price = input('请输入单价:')
# number = input('请输入数量:')
# print('商品总价是：',int(price)*int(number))

# is_hot = False
# is_cold = True
# is_rain = False

# if is_hot :
#     print('今天天气很热')
#     print('请多喝水')
# elif is_cold:
#     print('今天天气很冷')
#     print('注意保暖')
# elif is_rain:
#     print('今天有雨')    
#     print('记得带伞')
# else:    
#     print('今天是好天气')  
# print('祝你愉快')    

# username = input('请输入3-50个字符之间的用户名')
# # len(username) 获取字符串长度的用法
# # <3, >50
# if len(username) < 3:
#     print('用户名至少3个字符')
# elif len(username) > 50:
#     print('用户名不能超过50个字符')
# else:
#     print('用户名有效')    

# has_house = False
# has_car = False
# low_level = 0 
# if not low_level:
#     #考虑其他
#     if has_house and has_car:
#         print('非你莫属')
#     elif has_house or has_car:
#         print('非常满意')    
#     else:
#         print('满意')    
# else:
#     print('你不符合要求')        

# y = |x|
# x = 0
# if x >=0:
#     y = x
# else:
#     y = -x
# print(y)  
#       
# x = 1
# y = x if x >= 0 else -x
# print(y)

# a = 10 
# b = 2
# if a >= b:
#     c = a
# else:
#     c = b
# print(c)        

# 测试字符串
# 空字符串 ''  ""
# if '':
#     print('这是True')
# else:
#     print('这是False')

# 整形 0：False
# if 1:
#     print('这是True')
# else:    
#     print('这是False')

# # list, tuple, dict, set
# if set():
#     print('这是True')
# else:
#     print('这是False') 

# Object
# if None:
#     print('这是True')    
# else:
#     print('这是False')       

# while 循环
# i = 0
# while i < 3:
#     print(i)
#     i += 1

# 1+100=5050 while 循环
# i = 1 
# sum = 0
# while i <= 100:
#     sum += i    #sum = sum + i
#     i += 1

# print(sum)

# 99 乘法表 while
# i = 1
# while i <= 9:
#     #处理列数
#     j = 1
#     while j <= i:
#         print(j,'*', i, '=', j*i, end='  ')
#         j += 1
#     print('\n')
#     #使行数相加+1
#     i += 1

# # for 循环
# str_val = 'hello world'
# for item in str_val:
#     print(item)

# list_val = [13, 45, 564, 357, 4366, 34566]
# for item in list_val:
#     print(item)    

# value = range(0, 10, 2)    
# print (list(value))
 
# for i in range(3):
#      print(i)

# for循环 1+100的值   
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# for 循环的99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',j*i, end = '  ')
#     print('\n')    

# # break 跳出循环
# # 目标数字
# ecret_number = 8
# # 猜的最多次数
# guess_limit = 3
# # 已猜测次s数
# guess_number = 0
# while guess_number < guess_limit:
#     guess = int(input('请输入0-9之间的数字:'))
#     guess_number += 1
#     if guess == secret_number:
#         print('恭喜你，你赢了')
#         break

# print('游戏结束')

# # 循环嵌套使用break
# for i in range(1,10):
#     for j in range(1, i+1):
#         if j == 6:
#             break
#         print(j,'*',i,'=',i*j,end ='  ')
#     print() 

# 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',j*i, end="  ")
#     print('\n')

# 66乘法表
# for i in range(1,10):
#     if i == 7:
#         break
#     for j in range(1,i+1):
#         print(j,'*',i,'=',j*i,end='  ')
#     print()     

# 1-100的奇数
# for i in range(1,101,2):
#     print(i)


# 1-100之间的各种数字
# for i in range(1, 101):
#     if i%2 == 0:
#     print(i)    
            
#单引号建字符串
# name = 'anndy'

# #双引号建字符
# hoby = "baskball"

# #三个单引号或三个双引号
# zen = '''
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# '''
# print(zen)

# print('anndy\'s hobby is baskball')
# print("anndy's hobby is baskball")
# print('I say:"life is short and hard, I use python"')

# motto = '积善之家, 必有余庆.'

# word = 'python'
# word[0]
# 'j'+word[1:]

#join()函数
list_val = ['www','baidu','com']
str_val = '.'·join(list_val)
print(str_val)

tuple = ('users','world','cold')
str_val = '/'·join(tuple)
print(str_val)