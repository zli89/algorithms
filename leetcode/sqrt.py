"""
implement sqrt(x)
"""
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0 or x == 1:
            return x
        low = 0
        high = (x / 2) + 1    # sqrt(x) is between 0 and x/2
        while high - low > 1:    # we want loop stop when k^2 <= x and (k+1)^2 > x
            mid = (low + high) / 2
            square_mid = mid ** 2
            if square_mid == x:
                return mid
            if square_mid < x:
                low = mid
            elif sqaure_mid > x:
                hight = mid
        return low
