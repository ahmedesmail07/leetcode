class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {} # this hashmap contains nothing initially...
        # using enumerate to loop inside the list AS INT VALUES
        for i , j in enumerate(nums):
            diff = target - j 
            if diff in Map:
                # return the solution
                return [Map[diff],i]
            Map[j] = i
        return []