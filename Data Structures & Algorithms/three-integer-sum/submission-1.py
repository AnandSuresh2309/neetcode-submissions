class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p1 = 0
        nums.sort()
        res = set()
        while p1 <= len(nums)-3:
            p2 = p1+1
            p3 = len(nums)-1
            while p2 < p3:
                if nums[p1] + nums[p2] + nums[p3] < 0:
                    p2+=1
                elif nums[p1] + nums[p2] + nums[p3] > 0:
                    p3-=1
                else:
                    val = (nums[p1], nums[p2], nums[p3])
                    res.add(val)
                    p2+=1
                    p3-=1
            p1+=1
        return [list(i) for i in res]