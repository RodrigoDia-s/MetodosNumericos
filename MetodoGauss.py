from numpy import array, zeros, fabs, linalg


def gauss(a, b):
    a = array(a, float)
    b = array(b, float)
    n = len(b)

    print("\nSolução do numpy")
    print(linalg.solve(a, b))

    for k in range(n):
        # Pivotização parcial
        if fabs(a[k, k]) < 1.0e-12:
            for i in range(k + 1, n):
                if fabs(a[i, k]) > fabs(a[k, k]):
                    for j in range(k, n):
                        a[k, j], a[i, j] = a[i, j], a[k, j]
                    b[k], b[i] = b[i], b[k]
                    print("Foi necessário a troca de linhas, a matriz após essas operações ficou: \n",a, b)
                    break
        # divisão do pivo
        pivo = a[k, k]
        for j in range(k, n):
            a[k, j] /= pivo
        b[k] /= pivo
        # Loop de eliminação
        for i in range(n):
            if i == k or a[i, k] == 0: continue
            factor = a[i, k]
            for j in range(k, n):
                a[i, j] -= factor * a[k, j]
            b[i] -= factor * b[k]
            print("Matriz modificada: \n", a, "\n", b)
    return b, a



while(1):
    questao = int(input("Digite 1 para calcular uma solução de sistema\nOu 2 para fechar o programa:\n"))
    if questao == 1:
        valor = int(input("Digite o valor de linhas e colunas de sua matriz singular: "))
        if valor > 1:
            a = []
            b = []
            for i in range(valor):
                linha = []
                for j in range(valor):
                    elemento = input("Elemento linha {} e coluna {}: ".format(i, j))
                    linha.append(float(elemento))
                a.append(linha)
            for i in range(valor):
                elemento = input("valor da matriz resultado: {} ".format(i))
                b.append(float(elemento))
            print("\nMatriz 1:\n", a)
            print("Vetor:", b)

            X, A = gauss(a, b)
            print("\n-----Solução:-----\n", X)
            print("Sistema modificado \n", A)
        else:print("Não tem como fazer né")
    else:
     exit(1)
