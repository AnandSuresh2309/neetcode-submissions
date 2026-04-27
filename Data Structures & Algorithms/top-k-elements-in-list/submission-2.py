class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count, bucket = defaultdict(),defaultdict(list)
        for i in nums:
            count[i]  = count.get(i,0)+1
        for key,v in count.items():
            bucket[v].append(key)
        for x in range(len(nums),0, -1):
            if bucket.get(x,0):
                res.extend(bucket[x])
                if k == len(res):
                    return res

        