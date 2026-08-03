class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, minimal = 0, inf
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - minimal)
            minimal = min(minimal, prices[i])
        return max_profit