from pathlib import Path


folder01 = Path('ecommerce')
print(folder01.exists())  # 返回布尔值表示目录是否存在

root_path = Path()
for this_file in root_path.glob('*.py'):
    print(this_file)


