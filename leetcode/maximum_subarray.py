"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
import sys
class Solution:
    # @param A, a list of integers
    # @return an integer
    def max_subarray_dp(self, A):
        """
        dynamic programming
        scan through the array values, computing at each position
        the max subarray ending at that position.

        O(n)
        """
        max_ended_here = max_so_far = A[0]
        for x in A[1:]:
            max_ended_here = max(max_ended_here + x, x)
            max_so_far = max(max_so_far, max_ended_here)
        return max_so_far

    def merge(self, l, r):
        """
        left_sum is the max sum ending at the last element
        of the left array.
        right_sum is the max sum starting at the first element
        of the right array.
        The max is the sum of left_sum and right_sum.

        O(n)
        """
        s = 0
        left_sum = -sys.maxint - 1
        for x in reversed(l):
            s += x
            left_sum = max(left_sum, s)
        s = 0
        right_sum = -sys.maxint - 1
        for x in r:
            s += x
            right_sum = max(right_sum, s)
        return left_sum + right_sum

    def max_subarray_dc(self, A):
        """
        divide and comquer
        computer the max in left and right halves
        and when merge, computer the max crossing midpoint.
        Return the max of the three.

        O(nlogn)
        """
        if len(A) == 1:
            return A[0]
        left_max = self.max_subarray_dc(A[:len(A)//2])
        right_max = self.max_subarray_dc(A[len(A)//2:])
        cross_max = self.merge(A[:len(A)//2], A[len(A)//2:])
        return max(left_max, right_max, cross_max)
