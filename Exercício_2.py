def matriz_multiplicador(A, B):
    if len(A[0]) != len(B):
        print("Erro: O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        return None
    
    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


A = [[3, 1, 3], [6, 5, 5]] 
B = [[100, 50], [50, 100], [50, 50]]  

C = matriz_multiplicador(A, B)  


print("Matriz A:")
for row in A:
    print(row)

print("Matriz B:")
for row in B:
    print(row)

print("Produto de A e B:")
for row in C:
    print(row)