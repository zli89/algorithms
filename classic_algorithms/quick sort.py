from random import randint

def qsort(l, r, a):
    if l >= r:
        return
    i = l
    j = r
    t = randint(l, r)
    p = a[t]

    while True:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        if i < j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        else:
            break
    qsort(l, j, a)
    qsort(j+1, r, a)
