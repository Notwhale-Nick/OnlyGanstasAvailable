A = [0] * 10

print("Введите 10 чисел:")
for i in range(10):
    A[i] = int(input())

result = 1
pos = False

for i in range(10):
    if A[i] > 0:
        result = result * A[i]
        pos = True

if pos:
    print(result)
else:
    print(0)
