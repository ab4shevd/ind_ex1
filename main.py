import random

def generate_random_list():
    random_list = [random.randint(5, 100) for _ in range(11)]
    return random_list
