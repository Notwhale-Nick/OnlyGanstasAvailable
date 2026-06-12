flight = []

n = int(input("Сколько рейсов ввести? "))

for i in range(n):
    print(f"\nРейс {i+1}:")
    destination = input("Пункт назначения: ")
    num = input("Номер рейса: ")
    type = input("Тип самолёта: ")
    flight.append({"destination": destination, "num": num, "type": type})

flight.sort(key=lambda x: x["num"])

print("\nСписок рейсов (по возрастанию номера):")
for r in flight:
    print(f"{r['num']} -> {r['destination']} ({r['type']})")

search = input("\nВведите пункт назначения для поиска: ")

found = False
print("\nРезультат:")
for r in flight:
    if r["destination"] == search:
        print(f"Рейс {r['num']}, самолёт {r['type']}")
        found = True

if not found:
    print("Рейсов в этот пункт назначения нет")
