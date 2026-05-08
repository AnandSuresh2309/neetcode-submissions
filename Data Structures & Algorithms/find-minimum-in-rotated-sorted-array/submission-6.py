class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        print(l,mid,r)
        while r!=l:
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
            mid = (l+r)//2
            print(l,mid,r)
        return nums[l]