class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = [0] * 10       #as there are 10 possible digits from 0 to 9

        for digit in str(n):
            freq[int(digit)] += 1

        return sum(d * freq[d] for d in range(10))