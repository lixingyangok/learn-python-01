for cur in range(1, 99):
    condition1 = cur % 3 == 0
    condition2 = cur % 7 == 0
    condition3 = cur > 10
    condition4 = cur < 50
    if condition1 and condition2 and condition3 and condition4:
        print(cur)

print('I have learned git')