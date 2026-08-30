class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        MinVar = float('inf')
        MaxVar = float('-inf')
        minMaxIndexList = [0, 0]

        for i in range(n):
            if nums[i] < MinVar:
                MinVar = nums[i]
                minMaxIndexList[0] = i

            if nums[i] > MaxVar:
                MaxVar = nums[i]
                minMaxIndexList[1] = i

        left = min(minMaxIndexList)
        right = max(minMaxIndexList)

        # 3 possibilities:
        # 1. Remove both from front
        front = right + 1

        # 2. Remove both from back
        back = n - left

        # 3. Remove one from front and one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)