class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            num_arr = [0] * 26
            for c in i:
                num_arr[ord(c)-ord('a')] += 1
            dic[tuple(num_arr)].append(i)

        return [i for i in dic.values()]
