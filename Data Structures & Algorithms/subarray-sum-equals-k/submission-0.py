class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s_dict = {}
        s_dict[0] = 1
        res =cursum= 0
        for i in range(len(nums)):
            cursum+=nums[i]
            if cursum - k in s_dict:
                res+= s_dict[cursum-k]
            s_dict[cursum] = s_dict.get(cursum,0) +1
        return res 
