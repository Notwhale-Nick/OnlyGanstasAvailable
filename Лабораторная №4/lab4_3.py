tup = tuple(map(int, input("Введите элементы кортежа через пробел: ").split()))

uporyadochen = True
first_bad_index = -1

for i in range(len(tup) - 1):
    if tup[i] > tup[i + 1]:  
        uporyadochen = False
        first_bad_index = i + 1  
        break

if uporyadochen:
    print("Кортеж упорядочен по возрастанию")
else:
    print("Кортеж НЕ упорядочен")
    print("Номер первого нарушающего элемента:", first_bad_index)
