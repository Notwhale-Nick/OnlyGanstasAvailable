price = {
    "монитор": float(input("Монитор: ")),
    "системный блок": float(input("Системный блок: ")),
    "клавиатура": float(input("Клавиатура: ")),
    "мышь": float(input("Мышь: ")),
}

one_pc = sum(price.values())

n = int(input("\nКоличество компьютеров: "))

print(f"\n1 компьютер = {one_pc} руб.")
print(f"3 компьютера = {one_pc * 3} руб.")
print(f"{n} компьютеров = {one_pc * n} руб.")
