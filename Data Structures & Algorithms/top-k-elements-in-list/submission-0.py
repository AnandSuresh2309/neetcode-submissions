class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        cnt = sorted([i for i in dic.items()], key = lambda x : x[1], reverse = True)[:k]

        return list(map(lambda x:x[0], cnt))


        