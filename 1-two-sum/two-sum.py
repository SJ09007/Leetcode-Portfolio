class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   
        dict1={}
        for curr_index,val in enumerate(nums):
            required=target-val
            if required in dict1:
                return[dict1[required],curr_index]
            dict1[val]=curr_index