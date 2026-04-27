class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(n):
            le = len(n)
            if le == 1:
                return n
            else:
                l = merge(n[:le//2])
                r = merge(n[le//2:])
                temp = []
                lp = rp = 0
                for i in range(le):
                    if lp < len(l) and rp < len(r):
                        if l[lp] < r[rp]:
                            temp.append(l[lp])
                            lp += 1
                        else:
                            temp.append(r[rp])
                            rp += 1
                    elif lp < len(l):
                        temp.append(l[lp])
                        lp += 1
                    else:
                        temp.append(r[rp])
                        rp += 1
                return temp
        return merge(nums)
