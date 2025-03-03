import random

def generate_random_list():
    random_list = [random.randint(5, 100) for _ in range(11)]
    return random_list

# Тестирование функциии и добавление gitignore
random_list = generate_random_list()
print(random_list)
print("The program is finished")