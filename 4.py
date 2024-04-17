import random

correct = 0
mistakes = 0

while mistakes < 3:
    ch1 = random.randint(1, 10)
    ch2 = random.randint(1, 10)
    result = ch1 + ch2

    k = input(f"{ch1} + {ch2} = ")

    if  int(k) == result:
        print("Правильно")
        correct += 1
    else:
        print("Ответ неверный")
        mistakes += 1

print(f"Игра окончена. Правильных ответов: {correct}")
