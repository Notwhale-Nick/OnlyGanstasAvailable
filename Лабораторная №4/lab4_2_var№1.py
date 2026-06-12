A = list(map(float, input("Введите элементы списка через пробел: ").split()))

sum_neg = 0
for x in A:
    if x < 0:
        sum_neg = sum_neg + x
print("Сумма отрицательных:", sum_neg)

max_index = 0
min_index = 0
for i in range(len(A)):
    if A[i] > A[max_index]:
        max_index = i
    if A[i] < A[min_index]:
        min_index = i

left = min(max_index, min_index)
right = max(max_index, min_index)

rand = 1
if right - left > 1:  
    for i in range(left + 1, right):
        rand = rand * A[i]
else:
    rand = 0
print("Произведение между max и min:", rand)

A.sort()
print("Упорядоченный список:", A)
