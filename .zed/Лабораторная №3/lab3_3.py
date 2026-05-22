total = 64

print("Возможные сочетания:")
print("   Гуси  |  Кролики")

for rabbits in range(0, total // 4 + 1):
    rabbits_legs = rabbits * 4
    remaining_legs = total - rabbits_legs

    if remaining_legs % 2 == 0:
        geese = remaining_legs // 2
        print(f"   {geese:3}   |   {rabbits:3}")

max_rabbits = total // 4
print(f"\nМаксимум кроликов: {max_rabbits} (гусей при этом: 0)")
print(f"Максимум гусей: {total // 2} (кроликов при этом: 0)")
