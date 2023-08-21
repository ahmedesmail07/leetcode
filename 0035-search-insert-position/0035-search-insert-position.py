class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i
            else:
                i+= 1
        return len(nums)
        