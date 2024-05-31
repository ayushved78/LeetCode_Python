class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams_map[sorted_s].append(s)
        return list(anagrams_map.values()) 