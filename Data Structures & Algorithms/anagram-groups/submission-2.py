class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for s in strs:
            t= 26*[0]
            for i in s:
                t[ord(i)-ord('a')] += 1
            dict[tuple(t)].append(s)
        return list(dict.values())
        