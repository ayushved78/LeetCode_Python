class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        merged = []
        for i in range(0,min_len):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.extend(word1[min_len:])
        merged.extend(word2[min_len:])

        return ''.join(merged)