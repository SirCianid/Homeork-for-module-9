first_list = ['Strings', 'Student', 'Computers']
second_list = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first_list, second_list) if len(x) != len(y))
second_result = (len(first_list[i]) > len(second_list[i]) for i in range(min(len(first_list), len(second_list))))

print(list(first_result))
print(list(second_result))
