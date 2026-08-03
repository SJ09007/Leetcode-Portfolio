class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for x in nums:
            if x not in a:
                a.add(x)
            else:
                return True
        return False