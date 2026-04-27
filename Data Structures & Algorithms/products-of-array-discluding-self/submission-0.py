class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        suf = [1]*len(nums)
        res = []
        for i in range(1,len(nums)):
            pre[i] = nums[i-1] * pre[i-1]
            
        for j in range(len(nums)-2,-1,-1):
            suf[j] = nums[j+1] * suf[j+1]
        
        for k in range(len(nums)):
            res.append(pre[k]*suf[k])
        return res

