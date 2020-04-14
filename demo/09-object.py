person01 = {  # dictionary
    'name': 'Tom',
    'age': 18,
    'has_graduate': False,
}

print(person01['name'] + '\n')
person01['name'] = 'Jack'  # 修改
person01['nickname'] = 'Tiger'  # 新增

print('name, nickname = ', person01['name'], person01['nickname'] + '\n')
print('age = ', person01.get('age'))

# print(person01['other'])  # 取不值，报错
print('is_married = ', person01.get('is_married'))  # 取不到值，返回none
print('is_married = ', person01.get('is_married', False))  # 可提供默认值

numberObj = {
    '0': '零',
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '9': '九',
}
p_number = input('Type you phone number:　')
phone_number = ''
for this_one in p_number:
    phone_number += numberObj.get(this_one, '*')
print(phone_number)


word_lib = {
    'good': '😊',
    'bad': '😢',
}
mood = input('Type you mood:　')
mood = mood.split(' ')
your_mood = ''
for this_word in mood:
    your_mood += word_lib.get(this_word, this_word) + ' '
print(your_mood)
