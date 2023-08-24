class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for char_group in zip(*strs):
            if len(set(char_group)) == 1:
                result += char_group[0]
            else:
                break
        return result
