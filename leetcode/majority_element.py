"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def hash_table(self, num):
        """
        mantain a hash table of the counts of each element

        O(n)
        """
        d = {}
        for n in num:
            d[n] = 1 if d.get(n) == None else d[n]+1
            if d[n] > len(num)//2:
                return n

    def divide_and_conquer(self, num):
        """
        global majority must be either left half majority or
        right half majority. When "merge", count the two
        candidates to select one.

        O(nlogn)
        """
        if len(num) == 1:
            return num[0]
        x = self.divide_and_conquer(num[:len(num)//2])
        y = self.divide_and_conquer(num[len(num)//2:])
        if x == y:
            return x
        i = 0
        j = 0
        for n in num:
            if n == x:
                i += 1
            elif n == y:
                j += 1
        return x if i > j else y

    def voting(self, num):
        """
        Moore's voting algorithm only works when the list
        has a majority - more than half of the elements
        beging the same.

        O(n)
        """
        candidate = num[0]
        count = 0
        for n in num:
            if count == 0:
                candidate = n
                count = 1
            else:
                if candidate == n:
                    count += 1
                else:
                    count -= 1
        return candidate

