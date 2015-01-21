import random

# merge two sorted arrays and count split inversions
def merge_and_countSplitInv(b, c):
    a = []
    z = 0
    i = 0
    j = 0
    while i < len(b) and j < len(c):    # iterate over b and c, append whichever less to a
    	if b[i] < c[j]:
    	    a.append(b[i])
    	    i += 1
    	else:
    	    a.append(c[j])
    	    j += 1
    	    z += len(b) - i    # split inversions
    if i < len(b):    # append whichever remaining to a
    	a.extend(b[i:])
    elif j < len(c):
    	a.extend(c[j:])
    return a, z

# given an array, return sorted array and number of inversions
def merge_sort_and_countInv(a):
    if len(a) == 1:    # if only one element, no need to sort and no inversions
        return a, 0
    (b, x) = merge_sort_and_countInv(a[:len(a)//2])    # sort left half and count left inner inversions
    (c, y) = merge_sort_and_countInv(a[len(a)//2:])    # sort right half and count right inner inversions
    (a, z) = merge_and_countSplitInv(b, c)    # merge two sorted halves and count split inversions
    return a, x+y+z    # return sorted array and total inversions which equals 
                       # the sum of inner and split inversions

print(merge_sort_and_countInv(random.sample(range(1, 7), 6)))
