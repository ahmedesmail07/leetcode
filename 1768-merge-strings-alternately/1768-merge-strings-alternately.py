class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(len(word1)):
            result.append(word1[i])
            for j in range(len(word2)):
                if j == i :
                    result.append(word2[j])
        result.extend(word2[len(word1):]) 
        return "".join(result)