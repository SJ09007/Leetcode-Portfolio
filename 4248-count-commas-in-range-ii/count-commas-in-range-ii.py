class Solution:
    def countCommas(self, n: int) -> int:        
        # Numbers from 1000 to n
        ans=0
        if n >= 1000:
            ans += n - 999
        
        # Numbers from 1,000,000 to n
        if n >= 1000000:
            ans += n - 999999
        
        # Numbers from 1,000,000,000 to n
        if n >= 1000000000:
            ans += n - 999999999
        
        # Numbers from 1,000,000,000,000 to n
        if n >= 1000000000000:
            ans += n - 999999999999
        
        # Numbers from 1,000,000,000,000,000 to n
        if n >= 1000000000000000:
            ans += n - 999999999999999
        
        return ans