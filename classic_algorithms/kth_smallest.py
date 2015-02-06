import random

"""
linear time selection
"""

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def partition(a, l, r):
    p = a[l]    # for a better pivot, randomly choose one
    i = l + 1
    for j in range(l+1, r):
        if a[j] < p:
            swap(a, i, j)
            i += 1
    swap(a, l, i-1)
    return i


def kth(a, n, th):
    if n == 1:
        return a[0]
    p = partition(a, 0, n)
    if p == th:
        return a[p-1]
    elif p < th:
        return kth(a[p:], n-p, th-p)
    else:
        return kth(a[:p-1], p-1, th)


b = random.sample(range(1, 100), 5)
th = 1
print(kth(b, len(b), th))
