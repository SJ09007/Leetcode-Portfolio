class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(len(nums)):    
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums


'''

using 2 pointer approach
        1 0 2 3 4 0 8 
        L
        R

        1 0 2 3 4 0 8 
        L
         R

        1 0 2 3 4 0 8 
          L
          R

        1 0 2 3 4 0 8 
          L
           R

        1 2 0 3 4 0 8 
            L
              R

              and so on

        
        1 2 3 4 8 0 0 
                  L
                    R

'''   
