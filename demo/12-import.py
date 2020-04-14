# ▼精确导入
from demo.fnlib import get_sum
fn_list = __import__('10-function')
# ▲导的文件会执行其中的方法


print('\n以下是本文件打印的内容 ■■■■■■■■■■■■■■■■')
print(get_sum(3, 3))
print(fn_list.square(3))
fn_list.say_hi(
    last_name='Sawyer',
    first_name='Tom',
)
