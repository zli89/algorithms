"""
Implement pow(x, n)
"""

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    def fast_pow(self, x, n, ans):
        """
        x^n = (x^2)^(n/2) if n is even else x*x^(n-1)
        """
        if n == 0:
            return ans
        if n & 1:
            return self.fast_pow(x, n-1, ans*x)    # or return self.fast_pow(x*x, n//2, ans*x)
        else:
            return self.fast_pow(x*x, n//2, ans)

    def fast_pow_iteration(self, x, n):
        """ Iteration instead of recursion of fast_pow """
        ans = 1
        m = abs(n)
        while m != 0:
            if m & 1:
                ans *= x
            x = x * x
            m //= 2
        return 1/ans if n < 0 else ans

    def pow(self, x, n):
        ans = self.fast_pow(x, abs(n), 1)
        return 1/ans if n < 0 else ans
