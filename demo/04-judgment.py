is_hot = True
is_cold = False
msg = ''

if is_hot:
    msg = '天热 多喝水'
elif is_cold:
    msg = '天冷 多穿衣'
else:
    msg = '好天，多享受'
print('天气情况：', msg)

# ------------------------------------------------------------

if 2 > 1 and 2 > 1.5:
    print('你说的：全对')
else:
    print('你说的：不全对')

if 2 > 4 or 2 > 3:
    print('你说的：有一个对')
else:
    print('你说的，没一个对')

# ------------------------------------------------------------

is_good_credit = True
is_has_crime = False

if is_good_credit and not is_has_crime:
    print('通过：信用好，无不良记录')
