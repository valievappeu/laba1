import random
def num():
    true_answers = 0
    false_answers = 0
    while false_answers != 3:
        num1 = random.randint(-200, 200)
        num2 = random.randint(-200, 200)
        if num1 + num2 == int(input(f"{num1} + {num2} = ")):
            true_answers += 1
        else:
            false_answers += 1
    return f"Игра окончена. Правильных ответов: {true_answers}"
res = num()
print(res)