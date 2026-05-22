n = int(input("Введите возраст: "))

last_digit = n % 10
last_two_digits = n % 100

if 11 <= last_two_digits <= 14:
    word = "лет"
elif last_digit == 1:
    word = "год"
elif 2 <= last_digit <= 4:
    word = "года"
else:
    word = "лет"

print(f" {n} {word}")
