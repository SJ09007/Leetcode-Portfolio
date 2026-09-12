from collections import Counter
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        # The good array must have exactly n + 1 elements
        if len(nums) != n + 1:
            return False

        freq = Counter(nums)

        # n must appear exactly twice
        if freq[n] != 2:
            return False

        # Every number from 1 to n - 1 must appear exactly once
        for i in range(1, n):
            if freq[i] != 1:
                return False

        return True      