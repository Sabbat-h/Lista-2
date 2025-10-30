def fatorial(num):
     if num<=1:
          return 1
     else:
          return(num*fatorial(num-1))

A=[]
for i in range(6):
     A.append(int(input(f"Insira o {i + 1}° valor de A:")))

B=[]
for i in range (6):
     B.append(fatorial(A[i]))
     print(B[i])

