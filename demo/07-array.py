arr01 = [1, 2, 3]
arr01.insert(0, 0)  # 头部插入（指定位置），插入一个值
arr01.remove(0)  # 头部删除（指定位置）
print('arr01: ', arr01)

arr01.append(4)  # 尾部插入
arr01.append(5)
arr01.pop()  # 尾部删除
print('arr01: ', arr01)

arr01.clear()
print('arr01.clear(): ', arr01)

print('■' * 30)

arr01 = [7, 8, 9, 8]
arr02 = arr01[:]
arr03 = arr01.copy()
'''
●此时判断两者，还会相等
●删除新数组不会影响旧数组
'''

print('arr01: ', arr01)
print('arr01.index(8): ', arr01.index(8))  # 查询某值在数组中的【位置】（如果不在其中会报错
print('arr01.count(8): ', arr01.count(8))  # 查询某值在数组中的【数量】（找不到返回0
print('8 in arr01: ', 8 in arr01)  # 查询某值在数组中的【存在性】 返回布尔值

arr01.sort()
print('arr01.sort(): ', arr01)
arr01.reverse()
print('arr01.reverse(): ', arr01)



