# the_number = 5
# idx = 0
# while idx < 2:
#     your_number = int(input('Guess the number please: '))
#     if your_number == the_number:
#         print('You are right!')
#         break
#     idx += 1
# else:
#     print('You failed')

car_site = 0
while True:
    command = input('Type your order: ').lower()
    if command == 'quit':
        break
    elif command == 'go':
        car_site += 1
        print(f'The car stops at {car_site}')
    elif command == 'go back':
        car_site -= 1
        print(f'The car stops at {car_site}')
    elif command == 'stop':
        print(f'The car stops at {car_site}')
    else:
        print('Can\'t understand your order')
