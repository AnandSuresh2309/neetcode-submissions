class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,i in enumerate(nums):
            diff = target - i
            if diff in seen:
                return [seen[diff], idx]
            else:
                seen[i] = idx