class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        n = len(nums)

        # Check every subarray of size k
        for i in range(n - k + 1):
            window = set(nums[i:i + k])

            for x in window:
                count[x] = count.get(x, 0) + 1

        ans = -1

        # Find largest integer appearing in exactly one subarray
        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans