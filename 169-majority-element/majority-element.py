class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if count==0:
                element=nums[i]
            if nums[i]==element:            
                count+=1 
            else:
                count-=1
        return element
    #brute force : counting all (O(n^2))
    #better : hashmap (store count and print max)
    #optimal : Moore's Votiong Algorithm (Apply Aglo then verify the majority element's count)
    #here verification isn't necessary for (n/2) as it is given that there already exists an element with count greater than n/2
    #Solving using Moore's Voting Algorithm
    