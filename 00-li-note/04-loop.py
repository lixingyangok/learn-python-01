"""
遍历一切
"""

# 遍历字符
print('遍历字符', end='：')
for cur in 'hello world':
    print(cur, end='-')
print()

# 遍历range
print('遍历range', end='：')
for cur in range(1, 6):
    print(cur, end='-')
print()

print('遍历序列', end='：')
for cur in [1,2,3]:
    print(cur, end="-")
print()


rangeVal = range(5)  # 声名一个range
rangeVal2 = range(0,10,2)
print(rangeVal, rangeVal2, sep='  <>  ')
print(list(rangeVal), list(rangeVal2), sep='  <>  ')  # 转为序列打印


theSum = 0
for cur in range(0, 100+1):
    theSum += cur
print(f"求和1-100：", theSum)


# ▼打印99表
# row = 1
# while row <= 9:
#     column = 1
#     while column <= row:
#         print(f'{column}*{row}={row*column}', end='\n' if column==row else '  ')
#         column += 1
#     row += 1
#
