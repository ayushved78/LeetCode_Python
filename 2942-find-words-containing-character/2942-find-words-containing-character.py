class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ar = []
        for i in range(len(words)):
            if x in words[i]:
                ar.append(i)
        return ar