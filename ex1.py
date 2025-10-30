A = []
for i in range(5):
    A.append(int(input(f"Insira o {i + 1}° valor de A:")))

B = []
for i in range(5):
    B.append(A[i] * 3)

print('O vetor B é:', B)
