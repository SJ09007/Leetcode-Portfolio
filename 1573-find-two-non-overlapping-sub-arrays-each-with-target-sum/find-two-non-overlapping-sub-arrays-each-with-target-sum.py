class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        # dp[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        dp = [float('inf')] * (n + 1)

        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Remove elements while sum is too large
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # We found a subarray with sum == target
            if curr_sum == target:
                length = right - left + 1

                # Best previous non-overlapping subarray
                if dp[left] != float('inf'):
                    ans = min(ans, length + dp[left])

                # This subarray can be the best one
                # for future subarrays
                dp[right + 1] = min(dp[right], length)
            else:
                dp[right + 1] = dp[right]

        return -1 if ans == float('inf') else ans