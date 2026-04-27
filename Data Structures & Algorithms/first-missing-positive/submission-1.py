class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx,i in enumerate(nums):
            if i < 0:
                nums[idx] = 0
        
        for idx in range(len(nums)):
            if 0 < abs(nums[idx]) <= len(nums):
                if nums[abs(nums[idx])-1] > 0:
                    nums[abs(nums[idx])-1] = 0 - nums[abs(nums[idx])-1]
            elif nums[idx] == 0:
                nums[idx] = (len(nums)+1)
        
        for j in range(len(nums)):
            if nums[j] > 0:
                return j+1
        return len(nums)+1

        