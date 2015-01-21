import random

def merge_and_countSplitInv(b, c):
    a = []
    z = 0
    i = 0
    j = 0
    while i < len(b) and j < len(c):
    	if b[i] < c[j]:
    	    a.append(b[i])
    	    i += 1
    	else:
    	    a.append(c[j])
    	    j += 1
    	    z += len(b) - 1
    if i < len(b):
    	a.extend(b[i:])
    elif j < len(c):
    	a.extend(c[j:])
    return a, z
    
def merge_sort_and_countInv(a):
    if len(a) == 1:
        return a, 0
    (b, x) = merge_sort_and_countInv(a[:len(a)//2])
    (c, y) = merge_sort_and_countInv(a[len(a)//2:])
    (a, z) = merge_and_countSplitInv(b, c)
    return a, x+y+z

print(merge_sort_and_countInv(random.sample(range(1, 7), 6)))
