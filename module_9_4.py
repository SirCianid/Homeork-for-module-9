from random import choice
# lambda-функция
first_string = 'Мама мыла раму'
second_string = 'Рамена мало было'

result1 = list(map(lambda x, y: x == y, first_string, second_string))
print(result1)


# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Привет', 'Здравствуй', 'Здарова', 'Хаю-хай', 'Конничивауте', 'Хеллоу')
print(first_ball())
print(first_ball())
print(first_ball())







