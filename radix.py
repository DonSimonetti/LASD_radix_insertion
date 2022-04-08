def countingSort(A):
    nMax = max(A)

    C = [0] * (nMax + 1)
    B = [0] * A.__len__()

    for i in range(A.__len__()):
        C[A[i]] += 1

    for i in range(1, C.__len__()):
        C[i] += C[i - 1]

    for i in range(A.__len__() - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B


def countingSortPerCipher(A, cifra=0, base=10):
    C = [0] * base
    B = [0] * A.__len__()

    for i in range(A.__len__()):
        C[int((A[i] / pow(base, cifra))) % base] += 1

    for i in range(1, C.__len__()):
        C[i] += C[i - 1]

    for i in range(A.__len__() - 1, -1, -1):
        B[C[int((A[i] / pow(base, cifra))) % base] - 1] = A[i]
        C[int((A[i] / pow(base, cifra))) % base] -= 1

    return B

def radixsort(A):
    # sottraggo il minimo
    arrMin = min(A)
    for i in range(A.__len__()):
        A[i] -= arrMin

    # calcolo numero di cifre
    n = max(A)

    base = 10
    cifre = 1
    while (n / base > 1):
        cifre += 1
        n=int(n/base)

    # ordinamento

    for i in range(cifre):
        A=countingSortPerCipher(A,i)

    # riaggiungo il minimo
    for i in range(A.__len__()):
        A[i] += arrMin

    return A
