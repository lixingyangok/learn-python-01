def say_hi(first_name, last_name):  # 定义了参数必须传参，不传报错
    print(f'Hi! {first_name} {last_name}')
    print('How are you?')


say_hi(  # 指定了参数名称之后，可以忽略顺序，Good
    last_name='Green',
    first_name='Jim',
)


#  ▼参数返回值
def square(number):
    return number * number


print(square(6))
