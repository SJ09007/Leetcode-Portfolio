from typing import List
from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:        

        a = [(i, j) for i, row in enumerate(img1)
             for j, x in enumerate(row) if x]

        b = [(i, j) for i, row in enumerate(img2)
             for j, x in enumerate(row) if x]

        return max(Counter((i - x, j - y) for i, j in a for x, y in b).values(), default=0)