"""
遍历的中断
"""

# continue跳过本次
print('跳过本次 continue', end='：')
for cur in range(10):
    if cur >= 3 and cur <= 6:
        continue
    print(cur, end='-')
print()

# break中断循环
print('中断循环 break', end='：')
for cur in range(10):
    if cur >= 5:
        break
    print(cur, end='-')
print()

# for else
print('循环无果安全 for else')
theNumber = '5'
for cur in range(3):
    typeIn = input('请输入数字：')
    if theNumber == typeIn:
        print('猜中了，', end='')
        break
else:  # 当上文中的循环体都完成了，则进入else阶段。如果遭遇 break 则 else 不会执行
    print('没有猜中，', end='')
print('游戏结束')