while True:
    word = input("Введите слово (или 'стоп' для завершения): ")
    if word.lower() == 'стоп':
        break
    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
