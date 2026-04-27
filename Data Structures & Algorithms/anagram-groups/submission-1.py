class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_of_list = {}
        for i in strs:
            key = [0]*26
            for j in i:
                key[ord(j)-ord('a')] += 1
                
            if tuple(key) in dict_of_list:
                dict_of_list[tuple(key)].append(i)
            else:
                dict_of_list[tuple(key)] = []
                dict_of_list[tuple(key)].append(i)
        
        return list(dict_of_list.values())