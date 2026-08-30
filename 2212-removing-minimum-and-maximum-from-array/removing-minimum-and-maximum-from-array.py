class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        MinVar = float('inf')
        MaxVar = float('-inf')
        minMaxIndexList = [0, 0]

        for i in range(len(nums)):
            if nums[i] < MinVar:
                MinVar = nums[i]
                minMaxIndexList[0] = i

            if nums[i] > MaxVar:
                MaxVar = nums[i]
                minMaxIndexList[1] = i

        return min(max(minMaxIndexList)+1,len(nums)-min(minMaxIndexList) , (len(nums)-max(minMaxIndexList))+(min(minMaxIndexList)+1) )

'''
since integers are distinct is given , can we just take 2 vars 
Minvar=inf
MaxVar=-inf
and a list minMaxIndexList=[0,0]
traverse through the array and store/update indices of min and max var 
then 3 possibilites hogi , ya toh max(minMaxIndexList)+1 , ya toh len(nums)-min(minMaxIndexList) , ya toh (len(nums)-max(minMaxIndexList))+(min(minMaxIndexList)+1)

inn teeno ka min answer hoga
'''