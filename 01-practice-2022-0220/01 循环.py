
d01 = { 'key01': 1, 'key02': 2 }

# enumerate 用在字典上表现不佳
print('-'*33)
for idx, key in enumerate(d01): 
    print(idx, key)
# 打印：0 key01
# 打印：1 key02

print('-'*33)
for key in d01:
    print(key)

print('-'*33)
for key in d01.keys():
    cur = d01[key]
    print(key, cur)



