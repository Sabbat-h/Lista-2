A = []
for i in range(2):
    A.append(int(input(f'Insira o {i + 1}° valor de A:')))
B = []
for i in range(3):
    B.append(int(input(f'Insira o {i + 1}° valor de B:')))
C = []
for i in range (5):
    if i < 2:
        C.append(A[i])
    else:
        C.append(B[i-2])

print(C)
