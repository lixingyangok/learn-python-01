'''
Author: 李星阳
Date: 2022-02-20 20:27:25
LastEditors: 李星阳
LastEditTime: 2022-02-20 20:40:38
Description: 
'''
import math

print(
    f'\n■■ 取整 {"■"*30}',
    f'// 向下取整(得到浮点)： {1.999999 // 1}', # 1
    f'// 向上取整(得到浮点)： {1.999999 // 1 + 1}', # 2
    f'math 向下取整： {math.floor(1.999999)}', # 1
    f'math 向上取整： {math.ceil(1.000001)}', # 2
    f'四舍五入取整： {round(1.4)}', # 1 会返回浮点数
    f'四舍五入取整： {round(1.5)}', # 2
    sep='\n'
)



piVal = 3.141592653
print('The pi is: ', f"{piVal:.2f}") # 3.14



