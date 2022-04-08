def countingsort(A):
    n_max = max(A)

    C = [0] * (n_max + 1)
    B = [0] * A.__len__()

    for i in range(A.__len__()):
        C[A[i]] += 1

    for i in range(1, C.__len__()):
        C[i] += C[i - 1]

    for i in range(A.__len__() - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B


def countingsort_per_cipher(A, cifra=0, base=10):
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
    arr_min = min(A)
    for i in range(A.__len__()):
        A[i] -= arr_min

    # calcolo numero di cifre
    n = max(A)

    base = 10
    cifre = 1
    while n / base > 1:
        cifre += 1
        n = int(n / base)

    # ordinamento

    for i in range(cifre):
        A = countingsort_per_cipher(A, i)

    # riaggiungo il minimo
    for i in range(A.__len__()):
        A[i] += arr_min

    return A
