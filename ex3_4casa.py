A = []

for i in range(9):
    A.append(int(input('digite 1 valor:')))

a,b,c,d,e,f,g,h,i=A
A[1]=a
A[0]=b
A[7]=i
A[8]=h

print(A)