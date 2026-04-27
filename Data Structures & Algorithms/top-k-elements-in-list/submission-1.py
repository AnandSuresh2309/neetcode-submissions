class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        for key,val in freq.items():
            buckets[val].append(key)
        
        res = []

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res