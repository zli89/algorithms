"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
"""

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def binary_search(self, num, key):
        l = 0
        h = len(num) - 1
        while l <= h:
            m = (l + h) // 2
            if num[m] < key:
                l = m + 1
            elif num[m] > key:
                h = m - 1
            else:
                return key
        return None

    def three_sum_bi_search(self, num):
        """
        for the first two numbers, use binary search to find the third number

        O(n^2logn)
        """
        ans = set()
        num = sorted(num)
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                k = 0 - num[i] - num[j]
                f = self.binary_search(num[j+1:], k)
                if f is not None:
                    ans.add((num[i], num[j], k))    # set cannot add list
        ans = [list(a) for a in ans]
        return ans

    def three_sum_n2(self, num):
        """
        for every number in the list, find the other two.

        O(n^2)
        """
        ans = set()
        num = sorted(num)
        for i in range(len(num)-2):
            l = i + 1
            h = len(num) - 1
            while l < h:
                s = num[i] + num[l] + num[h]
                if s > 0:
                    h -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.add((num[i], num[l], num[h]))
                    l += 1    # find other possible triples
                    h -= 1
        ans = [list(a) for a in ans]
        return ans
