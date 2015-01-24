"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        """
        divide and conquer. Check middle element, if it is
        the target, return. Else if less than left neighbor,
        then target must exist in left half. Else target
        must lie in right half.

        O(logn)
        """
        if len(num) == 1:
            return 0
        if len(num) == 2:
            if num[0] > num[1]:
                return 0
            else:
                return 1
        m = len(num) // 2
        if num[m] > num[m-1] and num[m] > num[m+1]:
            return m
        if num[m] < num[m-1]:
            return self.findPeakElement(num[:m])
        else:
            return m+self.findPeakElement(num[m:])    # plus m to return index in the original array
