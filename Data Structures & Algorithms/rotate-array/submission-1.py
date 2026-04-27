class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        temp = nums[i]
        idx = 0
        start = 0
        while i < len(nums):
            if idx == start:
                idx = (idx+1)%len(nums)
                temp = nums[idx]
                start += 1
            x = (idx+k)%len(nums) 
            nums[x], temp = temp, nums[x]
            idx = x
            i += 1
