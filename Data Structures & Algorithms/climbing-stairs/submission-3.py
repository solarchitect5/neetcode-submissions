from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def paths(i):
            if i >= n:
                return (i == n)
            return paths(i+1) + paths(i+2)

        return paths(0)