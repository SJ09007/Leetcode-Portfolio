class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]

        l=0
        r=len(nums)-1

        while l<=r:
            if nums[l]*nums[l]>nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l+=1
            else:
                res.append(nums[r]*nums[r])
                r-=1

        return res[::-1]

'''
Solving in O(n) using the 2 pointer approach 
left pointer at nums[0] and right at the end 
then put the square of greatest of them at the end and keep updating pointers accordingly
building final array in the reverse order (we reverse it while returning)
we stop when left and right pointer cross each other (or are about to)
'''