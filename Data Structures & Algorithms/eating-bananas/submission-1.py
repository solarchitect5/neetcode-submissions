import math
from typing import List

def get_total_hours(piles: List[int], k: int) -> int:
    return sum(math.ceil(p / k) for p in piles)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Binary Search
        left = 1
        right = max(piles)
        result = max(piles)

        while left <= right: 
            mid = (left + right) // 2
            if get_total_hours(piles, mid) <= h:
                right = mid - 1
                result = mid
            else:
                left = mid + 1
        return result

        # Brute Force
        # k = 1
        # while k <= max(piles): 
        #     sum = 0
        #     for i in range(0, len(piles), 1): 
        #         sum = sum + math.ceil(piles[i] / k)
        #     if sum <= h:
        #         return k
        #     else:
        #         k += 1
        # return max(piles)
