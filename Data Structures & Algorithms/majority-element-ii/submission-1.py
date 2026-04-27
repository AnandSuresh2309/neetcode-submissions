class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, ct1, ct2 = 0, 0, 0, 0
        res = []
        for i in nums:
            if i == num1:
                ct1 += 1
            elif i == num2:
                ct2 += 1
            elif ct1 == 0:
                num1 = i
                ct1 += 1
            elif ct2 == 0:
                num2 = i
                ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1
        

        if nums.count(num1) > len(nums)/3:
            res.append(num1)

        if nums.count(num2) > len(nums)//3:
            res.append(num2)
        
        return res



