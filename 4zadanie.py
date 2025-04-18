group1 = ["Иванов", "Смирнова", "Кузнецов", "Васильев", "Петрова", "Волкова", "Попов", "Петров", "Лебедев", "Козлов"]
group2 = ["Николаев", "Орлов", "Андреев", "Макаров", "Никитин", "Захаров", "Зайцев", "Соловьев", "Борисов", "Романова"]
import random

team = tuple(random.sample(group1, 5) + random.sample(group2, 5))

print("Группа 1:", group1)
print("Группа 2:", group2)
print("Спортивная команда:", team)

print("Длина команды:", len(team))

sorted_team = tuple(sorted(team))
print("Отсортированная команда:", sorted_team)

if "Иванов" in team:
    count_ivanov = team.count("Иванов")
    print(f"Студент 'Иванов' входит в команду. Количество вхождений: {count_ivanov}")
else:
    print("Студент 'Иванов' не входит в команду.")