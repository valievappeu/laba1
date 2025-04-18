# Создаем словарь стран и столиц
countries = {
    'Россия': 'Москва',
    'Германия': 'Берлин',
    'Франция': 'Париж',
    'Италия': 'Рим',
    'Япония': 'Токио',
    'Бразилия': 'Бразилиа',
    'Канада': 'Оттава',
    'Китай': 'Пекин'
}

# a) Выводим все пары ключ-значение
print("Все страны и их столицы:")
for country, capital in countries.items():
    print(f"{country}: {capital}")

print("\n" + "="*50 + "\n")

# b) Выводим столицу для конкретной страны (например, для Франции)
target_country = 'Франция'
print(f"Столица страны {target_country}: {countries.get(target_country, 'Страна не найдена')}")

print("\n" + "="*50 + "\n")

# c) Сортируем и выводим словарь по алфавиту стран
print("Страны и столицы в алфавитном порядке:")
for country in sorted(countries.keys()):
    print(f"{country}: {countries[country]}")