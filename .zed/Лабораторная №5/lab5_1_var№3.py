A = {"a", "h", "m", "o", "r"}
B = {"j", "k", "o", "u", "y"}
C = {"g", "h", "j"}
D = {"g", "j", "q"}

X = (A & C) | (D & B)
Y = (A & B) | (D - C)

print("X =", X)
print("Y =", Y)
