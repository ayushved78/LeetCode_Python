class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootSet = set(dictionary)
        def findRoot(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in rootSet:
                    return prefix
            return word    
        words = sentence.split()
        replacedWords = [findRoot(word) for word in words]
        return ' '.join(replacedWords)